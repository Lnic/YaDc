#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pss_entity as entity





# ---------- Constants ----------

ACHIEVEMENT_DESIGN_BASE_PATH = 'AchievementService/ListAchievementDesigns2?languagekey=fr'
ACHIEVEMENT_DESIGN_KEY_NAME = 'AchievementDesignId'
ACHIEVEMENT_DESIGN_DESCRIPTION_PROPERTY_NAME = 'AchievementTitle'










# ---------- Initialization ----------

achievements_designs_retriever: entity.EntityRetriever = entity.EntityRetriever(
    ACHIEVEMENT_DESIGN_BASE_PATH,
    ACHIEVEMENT_DESIGN_KEY_NAME,
    ACHIEVEMENT_DESIGN_DESCRIPTION_PROPERTY_NAME,
    'AchievementDesigns'
)
