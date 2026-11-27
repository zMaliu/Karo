-- Karo 初版数据库结构（MySQL 8 / InnoDB / utf8mb4）
-- 对应 功能实现规格书.md 初版范围；建表后可在 app/__init__.py 启用 db.create_all 或执行本文件。
-- 约定：时间存 UTC（DATETIME(3)）、软删除用 deleted_at、所有查询必须带 user_id。

CREATE TABLE IF NOT EXISTS user_account (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  phone         VARCHAR(20)  NOT NULL COMMENT '手机号（后续加密+盲索引）',
  nickname      VARCHAR(20)  NOT NULL DEFAULT '',
  avatar_url    VARCHAR(255) NOT NULL DEFAULT '',
  grade         VARCHAR(16)  NOT NULL DEFAULT '',
  major         VARCHAR(32)  NOT NULL DEFAULT '',
  goal          VARCHAR(128) NOT NULL DEFAULT '',
  status        VARCHAR(16)  NOT NULL DEFAULT 'active' COMMENT 'active/locked/deleted',
  last_login_at DATETIME(3)  NULL,
  created_at    DATETIME(3)  NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at    DATETIME(3)  NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_user_phone (phone),
  KEY idx_user_status (status)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='账号';

CREATE TABLE IF NOT EXISTS user_profile (
  id                    BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id               BIGINT UNSIGNED NOT NULL,
  personality           JSON NULL COMMENT '性格标签',
  habits                JSON NULL COMMENT '学习习惯',
  aesthetic             JSON NULL COMMENT '审美偏好',
  weakness              JSON NULL COMMENT '弱点标签',
  emotion_tendency      JSON NULL COMMENT '情感倾向',
  questionnaire_version VARCHAR(16) NOT NULL DEFAULT 'v0',
  completed_at          DATETIME(3) NULL,
  show_online           TINYINT(1) NOT NULL DEFAULT 1,
  personalized_rec      TINYINT(1) NOT NULL DEFAULT 1,
  push_enabled          TINYINT(1) NOT NULL DEFAULT 1,
  created_at            DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at            DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_profile_user (user_id),
  CONSTRAINT fk_profile_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='画像与隐私偏好';

CREATE TABLE IF NOT EXISTS user_device (
  id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id        BIGINT UNSIGNED NOT NULL,
  device_id      VARCHAR(64) NOT NULL,
  platform       VARCHAR(16) NOT NULL DEFAULT '',
  last_active_at DATETIME(3) NULL,
  revoked_at     DATETIME(3) NULL,
  created_at     DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_device_user (user_id, device_id),
  CONSTRAINT fk_device_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='登录设备';

CREATE TABLE IF NOT EXISTS timer_session (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id         BIGINT UNSIGNED NOT NULL,
  mode            VARCHAR(16) NOT NULL DEFAULT 'pomodoro' COMMENT 'pomodoro/focus',
  subject_tag     VARCHAR(32) NOT NULL DEFAULT '未分类',
  status          VARCHAR(16) NOT NULL DEFAULT 'ongoing' COMMENT 'ongoing/paused/completed/aborted',
  start_at        DATETIME(3) NOT NULL,
  end_at          DATETIME(3) NULL,
  paused_at       DATETIME(3) NULL,
  paused_sec      INT NOT NULL DEFAULT 0,
  duration_sec    INT NOT NULL DEFAULT 0,
  interrupted     TINYINT(1) NOT NULL DEFAULT 0,
  interrupt_count INT NOT NULL DEFAULT 0,
  note            VARCHAR(100) NOT NULL DEFAULT '',
  created_at      DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at      DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_session_user_status (user_id, status),
  KEY idx_session_user_start (user_id, start_at),
  CONSTRAINT fk_session_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='专注会话';

CREATE TABLE IF NOT EXISTS timer_checkin (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id      BIGINT UNSIGNED NOT NULL,
  checkin_date DATE NOT NULL,
  streak       INT NOT NULL DEFAULT 1,
  total_days   INT NOT NULL DEFAULT 1,
  created_at   DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at   DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_checkin_user_date (user_id, checkin_date),
  CONSTRAINT fk_checkin_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='每日签到与连签';

CREATE TABLE IF NOT EXISTS twin_profile (
  id            BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id       BIGINT UNSIGNED NOT NULL,
  avatar_id     VARCHAR(32) NOT NULL DEFAULT 'avatar_1',
  personality   JSON NULL,
  catchphrases  JSON NULL,
  weakness      JSON NULL,
  emotion       VARCHAR(16) NOT NULL DEFAULT 'calm' COMMENT 'happy/calm/anxious/crushed',
  intimacy      INT NOT NULL DEFAULT 0,
  mood_today    VARCHAR(16) NOT NULL DEFAULT '',
  created_at    DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at    DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_twin_user (user_id),
  CONSTRAINT fk_twin_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学伴配置';

CREATE TABLE IF NOT EXISTS twin_message (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    BIGINT UNSIGNED NOT NULL,
  role       VARCHAR(16) NOT NULL COMMENT 'user/assistant',
  content    TEXT NOT NULL,
  emotion    VARCHAR(16) NOT NULL DEFAULT '',
  created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_msg_user_time (user_id, created_at),
  CONSTRAINT fk_msg_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学伴消息';

CREATE TABLE IF NOT EXISTS brain_file (
  id           BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id      BIGINT UNSIGNED NOT NULL,
  title        VARCHAR(128) NOT NULL,
  file_type    VARCHAR(16) NOT NULL COMMENT 'pdf/image/word/txt',
  oss_url      VARCHAR(255) NOT NULL DEFAULT '',
  hash         VARCHAR(64) NOT NULL DEFAULT '',
  subject_tag  VARCHAR(32) NOT NULL DEFAULT '',
  parse_status VARCHAR(16) NOT NULL DEFAULT 'parsing' COMMENT 'parsing/ok/failed',
  summary      TEXT NULL,
  created_at   DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_file_user_hash (user_id, hash),
  CONSTRAINT fk_file_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='智脑文件';

CREATE TABLE IF NOT EXISTS brain_note (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    BIGINT UNSIGNED NOT NULL,
  title      VARCHAR(128) NOT NULL,
  content_md MEDIUMTEXT NOT NULL,
  tags       JSON NULL,
  version    INT NOT NULL DEFAULT 1,
  created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_note_user_time (user_id, created_at),
  CONSTRAINT fk_note_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Markdown 笔记';

CREATE TABLE IF NOT EXISTS brain_diary (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    BIGINT UNSIGNED NOT NULL,
  entry_date DATE NOT NULL,
  mood       VARCHAR(16) NOT NULL DEFAULT '',
  content    TEXT NOT NULL,
  created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_diary_user_date (user_id, entry_date),
  CONSTRAINT fk_diary_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学习日记';

CREATE TABLE IF NOT EXISTS brain_chunk (
  id          BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id     BIGINT UNSIGNED NOT NULL,
  source_type VARCHAR(16) NOT NULL COMMENT 'file/note/diary',
  source_id   BIGINT UNSIGNED NOT NULL,
  seq         INT NOT NULL DEFAULT 0,
  content     TEXT NOT NULL,
  created_at  DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_chunk_user_source (user_id, source_type, source_id),
  CONSTRAINT fk_chunk_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='切片（后续 RAG 用）';

CREATE TABLE IF NOT EXISTS solve_session (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id         BIGINT UNSIGNED NOT NULL,
  subject_tag     VARCHAR(32) NOT NULL DEFAULT '',
  source          VARCHAR(16) NOT NULL DEFAULT 'manual' COMMENT 'photo/manual',
  question_text   TEXT NOT NULL,
  image_url       VARCHAR(255) NOT NULL DEFAULT '',
  solution_steps  JSON NULL,
  final_answer    TEXT NULL,
  knowledge_tags  JSON NULL,
  model           VARCHAR(32) NOT NULL DEFAULT '',
  status          VARCHAR(16) NOT NULL DEFAULT 'solving' COMMENT 'solving/solved/failed',
  created_at      DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_solve_user_time (user_id, created_at),
  CONSTRAINT fk_solve_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='解题会话';

CREATE TABLE IF NOT EXISTS wrong_question (
  id              BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id         BIGINT UNSIGNED NOT NULL,
  session_id      BIGINT UNSIGNED NULL,
  question_text   TEXT NOT NULL,
  answer          TEXT NULL,
  knowledge_tags  JSON NULL,
  wrong_reason    VARCHAR(500) NOT NULL DEFAULT '',
  review_status   VARCHAR(16) NOT NULL DEFAULT 'new' COMMENT 'new/reviewed/mastered',
  reviewed_at     DATETIME(3) NULL,
  created_at      DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at      DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  KEY idx_wrong_user_status (user_id, review_status),
  CONSTRAINT fk_wrong_user FOREIGN KEY (user_id) REFERENCES user_account (id),
  CONSTRAINT fk_wrong_session FOREIGN KEY (session_id) REFERENCES solve_session (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='错题本';

CREATE TABLE IF NOT EXISTS palace_room (
  id         BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  user_id    BIGINT UNSIGNED NOT NULL,
  theme      VARCHAR(32) NOT NULL DEFAULT 'library',
  grid_w     INT NOT NULL DEFAULT 10,
  grid_h     INT NOT NULL DEFAULT 10,
  created_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_room_user (user_id),
  CONSTRAINT fk_room_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='宫殿房间';

CREATE TABLE IF NOT EXISTS palace_item (
  id             BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  room_id        BIGINT UNSIGNED NOT NULL,
  user_id        BIGINT UNSIGNED NOT NULL,
  item_type      VARCHAR(32) NOT NULL COMMENT 'bookshelf/desk/box/frame/plant/lamp',
  skin_id        VARCHAR(32) NOT NULL DEFAULT '',
  grid_x         INT NOT NULL DEFAULT 0,
  grid_y         INT NOT NULL DEFAULT 0,
  z_index        INT NOT NULL DEFAULT 0,
  link_type      VARCHAR(16) NOT NULL DEFAULT 'none' COMMENT 'file/note/wrong/none',
  link_id        BIGINT UNSIGNED NULL,
  name           VARCHAR(64) NOT NULL DEFAULT '',
  is_reward      TINYINT(1) NOT NULL DEFAULT 0,
  review_count   INT NOT NULL DEFAULT 0,
  last_review_at DATETIME(3) NULL,
  version        INT NOT NULL DEFAULT 1,
  created_at     DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
  updated_at     DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3) ON UPDATE CURRENT_TIMESTAMP(3),
  PRIMARY KEY (id),
  UNIQUE KEY uk_item_slot (room_id, grid_x, grid_y),
  KEY idx_item_user (user_id),
  CONSTRAINT fk_item_room FOREIGN KEY (room_id) REFERENCES palace_room (id),
  CONSTRAINT fk_item_user FOREIGN KEY (user_id) REFERENCES user_account (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='宫殿物品';

CREATE TABLE IF NOT EXISTS palace_skin (
  skin_id          VARCHAR(32) NOT NULL,
  item_type        VARCHAR(32) NOT NULL,
  image_url        VARCHAR(255) NOT NULL DEFAULT '',
  unlock_condition VARCHAR(128) NOT NULL DEFAULT '',
  PRIMARY KEY (skin_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='物品皮肤字典';
