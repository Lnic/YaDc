#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import urllib.parse

import emojis
import pss_assert
import pss_core as core
import pss_lookups as lookups
import pss_tournament as tourney
import pss_user as user
import settings
import utility as util


# ---------- Constants ----------

SEARCH_FLEETS_BASE_PATH = f'AllianceService/SearchAlliances?accessToken={settings.GPAT}&skip=0&take=100&name='
FLEET_KEY_NAME = 'AllianceId'
FLEET_DESCRIPTION_PROPERTY_NAME = 'AllianceName'

SEARCH_FLEET_USERS_BASE_PATH = f'AllianceService/ListUsers?accessToken={settings.GPAT}&skip=0&take=100&allianceId='





# ---------- Helper functions ----------

def get_fleet_details_by_info(fleet_info: dict) -> list:

    fleet_name = fleet_info[FLEET_DESCRIPTION_PROPERTY_NAME]
    fleet_description = fleet_info['AllianceDescription']
    min_trophy_required = fleet_info['MinTrophyRequired']
    member_count = int(fleet_info['NumberOfMembers'])
    trophies = int(fleet_info['Trophy'])
    stars = int(fleet_info['Score'])
    requires_approval = fleet_info['RequiresApproval'].lower() == 'true'
    division_design_id = fleet_info['DivisionDesignId']

    if requires_approval:
        fleet_type = 'Private'
    else:
        fleet_type = 'Public'
    division = lookups.DIVISION_DESIGN_ID_TO_CHAR[division_design_id]

    lines = [f'**{fleet_name}**']
    lines.append(f'```{fleet_description}')
    lines.append(f'Type - {fleet_type}')
    lines.append(f'Min trophies - {min_trophy_required}')
    lines.append(f'Members - {member_count}')
    lines.append(f'Trophies - {util.get_reduced_number_compact(trophies)}')
    if division != '-':
        lines.append(f'Division - {division}')
        lines.append(f'Stars - {util.get_reduced_number_compact(stars)}')

    lines[1] += '```'

    return lines


async def post_fleet_details(ctx, fleet_info: dict):
    output = get_fleet_details_by_info(fleet_info)
    if output:
        await util.post_output(ctx, output, settings.MAXIMUM_CHARACTERS)





# ---------- Alliance info ----------

def get_fleet_details_by_name(fleet_name: str, as_embed: bool = settings.USE_EMBEDS) -> list:
    pss_assert.valid_parameter_value(fleet_name, 'fleet_name', min_length=0)

    fleet_infos = _get_fleet_infos(fleet_name)
    fleet_ids = sorted([int(fleet_id) for fleet_id in fleet_infos.keys() if fleet_id])
    fleet_ids = [str(fleet_id) for fleet_id in fleet_ids]
    fleet_infos = [fleet_info for fleet_id, fleet_info in fleet_infos.items() if fleet_id in fleet_ids]
    return fleet_infos


def get_fleet_search_details(fleet_info: dict) -> str:
    fleet_name = fleet_info[FLEET_DESCRIPTION_PROPERTY_NAME]
    fleet_trophies = fleet_info['Trophy']
    fleet_stars = fleet_info['Score']
    fleet_division = int(fleet_info['DivisionDesignId'])
    trophies = f'  {emojis.trophy} {fleet_trophies}'
    if fleet_division > 0:
        stars = f'  {emojis.star} {fleet_stars}'
    else:
        stars = ''
    result = f'{fleet_name}{trophies}{stars}'
    return result


def _get_fleet_infos(fleet_name: str):
    fleet_data_raw = core.get_data_from_path(f'{SEARCH_FLEETS_BASE_PATH}{util.url_escape(fleet_name)}')
    fleet_infos = core.xmltree_to_dict3(fleet_data_raw)
    return fleet_infos




# ---------- stars command methods ----------



def get_top_100_raw():
    return None


def get_tournament_fleets_raw():
    return None









# ---------- Testing ----------

if __name__ == '__main__':
    test_fleets = ['Fallen An']
    for fleet_name in test_fleets:
        os.system('clear')
        is_tourney_running = tourney.is_tourney_running()
        fleet_infos = get_fleet_details_by_name(fleet_name)
        lines = [get_fleet_search_details(fleet_info) for fleet_info in fleet_infos]
        for line in lines:
            print(line)
