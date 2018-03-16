/*
PINNA
drop_tables.sql

Created by Shota Shimazu on 2018/03/05

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-serveur/blob/master/LICENSE
*/

DROP TABLE IF EXISTS artillery_pendingmail;
DROP TABLE IF EXISTS artillery_pendingmail_id_seq;
DROP TABLE IF EXISTS artillery_sentmail;
DROP TABLE IF EXISTS artillery_sentmail_id_seq;
DROP TABLE IF EXISTS auth_group;
DROP TABLE IF EXISTS auth_group_id_seq;
DROP TABLE IF EXISTS auth_group_permissions;
DROP TABLE IF EXISTS auth_group_permissions_id_seq;
DROP TABLE IF EXISTS auth_permission;
DROP TABLE IF EXISTS auth_permission_id_seq;
DROP TABLE IF EXISTS auth_user;
DROP TABLE IF EXISTS auth_user_groups;
DROP TABLE IF EXISTS auth_user_groups_id_seq;
DROP TABLE IF EXISTS auth_user_id_seq;
DROP TABLE IF EXISTS auth_user_user_permissions;
DROP TABLE IF EXISTS auth_user_user_permissions_id_seq;
DROP TABLE IF EXISTS django_admin_log;
DROP TABLE IF EXISTS django_admin_log_id_seq;
DROP TABLE IF EXISTS django_content_type;
DROP TABLE IF EXISTS django_content_type_id_seq;
DROP TABLE IF EXISTS django_migrations;
DROP TABLE IF EXISTS django_migrations_id_seq;
DROP TABLE IF EXISTS django_session;
DROP TABLE IF EXISTS grant_devicecredential;
DROP TABLE IF EXISTS grant_grantuser;
DROP TABLE IF EXISTS grant_grantuser_id_seq;
DROP TABLE IF EXISTS grant_onetaplogin;
DROP TABLE IF EXISTS grant_onetaplogin_id_seq;
DROP TABLE IF EXISTS grant_pendingresetaccount;
DROP TABLE IF EXISTS grant_pendingresetaccount_id_seq;
DROP TABLE IF EXISTS grant_signupverification;
DROP TABLE IF EXISTS grant_signupverification_id_seq;
DROP TABLE IF EXISTS message_room;
DROP TABLE IF EXISTS message_room_id_seq;
DROP TABLE IF EXISTS ping_compositiondetail;
DROP TABLE IF EXISTS ping_geolocationdetail;
DROP TABLE IF EXISTS ping_geolocationspotdetail;
DROP TABLE IF EXISTS ping_geolocationspotdetail_id_seq;
DROP TABLE IF EXISTS ping_pings;
DROP TABLE IF EXISTS ping_pingssongdetail;
DROP TABLE IF EXISTS pinlock_pubulishedlicense;
DROP TABLE IF EXISTS pinlock_pubulishedlicense_id_seq;
DROP TABLE IF EXISTS pinner_pinner;
DROP TABLE IF EXISTS pinner_pinner_id_seq;
DROP TABLE IF EXISTS serverless_lambda;
DROP TABLE IF EXISTS user_user;
DROP TABLE IF EXISTS user_user_id_seq;
DROP TABLE IF EXISTS user_userprofile;

-- WaveCloud Tables
DROP TABLE IF EXISTS wavecloud_soundcloudindexing;
DROP TABLE IF EXISTS wavecloud_soundcloudindexing_id_seq;

-- Serverless Tables
DROP TABLE IF EXISTS supervisor_admintheme;
DROP TABLE IF EXISTS supervisor_admintheme_id_seq;

-- Pages Tables
DROP TABLE IF EXISTS pages_helppages;
DROP TABLE IF EXISTS pages_landingpage;
DROP TABLE IF EXISTS pages_licensepage;
DROP TABLE IF EXISTS pages_richcontentspages;
DROP TABLE IF EXISTS pages_servingpages;
DROP TABLE IF EXISTS pages_simpletextpages;
