#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pss_entity as entity





# ---------- Constants ----------

MISSION_DESIGN_BASE_PATH = 'MissionService/ListAllMissionDesigns2?languagekey=fr'
MISSION_DESIGN_KEY_NAME = 'MissionDesignId'
MISSION_DESIGN_DESCRIPTION_PROPERTY_NAME = 'MissionTitle'










# ---------- Initialization ----------

missions_designs_retriever: entity.EntityRetriever = entity.EntityRetriever(
    MISSION_DESIGN_BASE_PATH,
    MISSION_DESIGN_KEY_NAME,
    MISSION_DESIGN_DESCRIPTION_PROPERTY_NAME,
    'MissionDesigns'
)
