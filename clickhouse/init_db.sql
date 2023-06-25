CREATE DATABASE IF NOT EXISTS ugc
ON CLUSTER company_cluster;

CREATE TABLE IF NOT EXISTS ugc.user_progress_queue
ON CLUSTER company_cluster
(
    user_id UUID,
    movie_id UUID,
    viewed_frame Int64,
    ts DateTime
)
ENGINE = Kafka
(
)
SETTINGS
    kafka_broker_list = 'broker:9092',
    kafka_topic_list = 'progress',
    kafka_group_name = 'clickhouse-group',
    kafka_format = 'JSONEachRow',
    kafka_num_consumers = 1;

CREATE TABLE IF NOT EXISTS ugc.user_progress
ON CLUSTER company_cluster
(
    user_id UUID,
    movie_id UUID,
    viewed_frame Int64,
    ts DateTime
)
ENGINE = MergeTree
PARTITION BY toYYYYMMDD(ts)
ORDER BY ts DESC;

CREATE MATERIALIZED VIEW IF NOT EXISTS ugc.user_progress_mv
TO ugc.user_progress AS
SELECT *
FROM ugc.user_progress_queue;
