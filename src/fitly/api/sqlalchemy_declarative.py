from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Float, BigInteger
from .database import Base


##### Athlete Table #####

class athlete(Base):
    __tablename__ = 'athlete'
    athlete_id = Column('athlete_id', Integer(), index=True, primary_key=True, autoincrement=True)
    name = Column('name', String(255))
    birthday = Column('birthday', Date())
    weight_lbs = Column('weight_lbs', Integer())
    resting_hr = Column('resting_hr', Integer())
    run_ftp = Column('run_ftp', Integer())
    ride_ftp = Column('ride_ftp', Integer())
    sex = Column('sex', String(1))
    min_non_warmup_workout_time = Column('min_non_warmup_workout_time',
                                         Integer())  # threshold in seconds for when we start counting workouts towards stress scores (don't want to include warm-ups)
    weekly_tss_goal = Column('weekly_tss_goal', Integer())
    rr_max_goal = Column('rr_max_goal', Integer())  # Max ramp rate threshold used for calculating injury risk
    rr_min_goal = Column('rr_min_goal', Integer())  # Min ramp rate threshold used for calculating injury risk
    weekly_workout_goal = Column('weekly_workout_goal', Integer())  # weekly workout minute goal
    weekly_sleep_score_goal = Column('weekly_sleep_score_goal', Integer())  # Oura sleep scores >= 85 to achieve weekly
    weekly_readiness_score_goal = Column('weekly_readiness_score_goal',
                                         Integer())  # Oura readiness scores >= 85 to achieve weekly
    weekly_activity_score_goal = Column('weekly_activity_score_goal',
                                        Integer())  # Oura activity scores >= 85 to achieve weekly
    daily_sleep_hr_target = Column('daily_sleep_hr_target', Integer())  # Daily sleep hour target
    ftp_test_notification_week_threshold = Column('ftp_test_notification_week_threshold',
                                                  Integer())  # Num weeks to retest ftp
    cycle_power_zone_threshold_1 = Column('cycle_power_zone_threshold_1', Float())
    cycle_power_zone_threshold_2 = Column('cycle_power_zone_threshold_2', Float())
    cycle_power_zone_threshold_3 = Column('cycle_power_zone_threshold_3', Float())
    cycle_power_zone_threshold_4 = Column('cycle_power_zone_threshold_4', Float())
    cycle_power_zone_threshold_5 = Column('cycle_power_zone_threshold_5', Float())
    cycle_power_zone_threshold_6 = Column('cycle_power_zone_threshold_6', Float())
    run_power_zone_threshold_1 = Column('run_power_zone_threshold_1', Float())
    run_power_zone_threshold_2 = Column('run_power_zone_threshold_2', Float())
    run_power_zone_threshold_3 = Column('run_power_zone_threshold_3', Float())
    run_power_zone_threshold_4 = Column('run_power_zone_threshold_4', Float())
    hr_zone_threshold_1 = Column('hr_zone_threshold_1', Float())
    hr_zone_threshold_2 = Column('hr_zone_threshold_2', Float())
    hr_zone_threshold_3 = Column('hr_zone_threshold_3', Float())
    hr_zone_threshold_4 = Column('hr_zone_threshold_4', Float())
    peloton_auto_bookmark_ids = Column('peloton_auto_bookmark_ids', String(9999))
    peloton_auto_bookmark_metric = Column('peloton_auto_bookmark_metric', String(10))


class hrvWorkoutStepLog(Base):
    __tablename__ = 'hrv_workout_step_log'
    id = Column('id', Integer(), index=True, primary_key=True, autoincrement=True)
    athlete_id = Column('athlete_id', Integer())
    date = Column('date', Date())
    hrv_workout_step = Column('hrv_workout_step', Integer())
    hrv_workout_step_desc = Column('hrv_workout_step_desc', String(20))
    completed = Column('completed', Boolean, default=False)
    rationale = Column('rationale', String(255))


class annotations(Base):
    __tablename__ = 'annotations'
    id = Column('id', Integer(), index=True, primary_key=True, autoincrement=True)
    athlete_id = Column('athlete_id', Integer())
    date = Column('date', Date())
    annotation = Column('annotation', String(255))


##### Strava Tables #####

class stravaSamples(Base):
    __tablename__ = 'strava_samples'
    timestamp_local = Column('timestamp_local', DateTime(), index=True, primary_key=True)
    time_interval = Column('time_interval', DateTime())
    activity_id = Column('activity_id', BigInteger())
    date = Column('date', Date())
    type = Column('type', String(255))
    act_name = Column('act_name', String(255))
    athlete_id = Column('athlete_id', BigInteger())
    distance = Column('distance', Float())
    velocity_smooth = Column('velocity_smooth', Float())
    temp = Column('temp', Float())
    altitude = Column('altitude', Float())
    latitude = Column('latitude', Float())
    longitude = Column('longitude', Float())
    heartrate = Column('heartrate', Integer())
    cadence = Column('cadence', Integer())
    watts = Column('watts', Integer())
    moving = Column('moving', Integer())
    grade_smooth = Column('grade_smooth', Float())
    ftp = Column('ftp', Float())
    time = Column('time', Integer())
    power_zone = Column('power_zone', Integer())
    hr_zone = Column('hr_zone', Integer())
    hr_lowest = Column('hr_lowest', Integer())


class stravaBestSamples(Base):
    __tablename__ = 'strava_best_samples'
    activity_id = Column('activity_id', BigInteger(), index=True, primary_key=True)
    interval = Column('interval', Integer, index=True, primary_key=True)
    mmp = Column('mmp', Float())
    ftp = Column('ftp', Float())
    watts_per_kg = Column('watts_per_kg', Float())
    timestamp_local = Column('timestamp_local', DateTime())
    time_interval = Column('time_interval', DateTime())
    type = Column('type', String(255))
    date = Column('date', Date())
    act_name = Column('act_name', String(255))
    athlete_id = Column('athlete_id', BigInteger())


class stravaSummary(Base):
    __tablename__ = 'strava_summary'
    start_date_utc = Column('start_date_utc', DateTime(), index=True, primary_key=True)
    activity_id = Column('activity_id', BigInteger())
    athlete_id = Column('athlete_id', BigInteger())
    name = Column('name', String(255))
    distance = Column('distance', Float())
    moving_time = Column('moving_time', BigInteger())
    elapsed_time = Column('elapsed_time', BigInteger())
    total_elevation_gain = Column('total_elevation_gain', Integer())
    type = Column('type', String(255))
    start_date_local = Column('start_date_local', DateTime())
    start_day_local = Column('start_day_local', Date())
    timezone = Column('timezone', String(255))
    start_lat = Column('start_lat', String(255))
    start_lon = Column('start_lon', String(255))
    end_lat = Column('end_lat', String(255))
    end_lon = Column('end_lon', String(255))
    location_city = Column('location_city', String(255))
    location_state = Column('location_state', String(255))
    location_country = Column('location_country', String(255))
    average_speed = Column('average_speed', Float())
    max_speed = Column('max_speed', Float())
    average_watts = Column('average_watts', Float())
    max_watts = Column('max_watts', Float())
    average_heartrate = Column('average_heartrate', Float())
    max_heartrate = Column('max_heartrate', Float())
    kilojoules = Column('kilojoules', Float())
    device_name = Column('device_name', String(255))
    calories = Column('calories', Float())
    description = Column('description', String(255))
    pr_count = Column('pr_count', Integer())
    achievement_count = Column('achievement_count', Integer())
    commute = Column('commute', Integer())
    trainer = Column('trainer', Integer())
    gear_id = Column('gear_id', String(255))
    ftp = Column('ftp', Float())
    weighted_average_power = Column('weighted_average_power', Float())
    relative_intensity = Column('relative_intensity', Float())
    efficiency_factor = Column('efficiency_factor', Float())
    tss = Column('tss', Float())
    hrss = Column('hrss', Float())
    variability_index = Column('variability_index', Float())
    trimp = Column('trimp', Float())
    low_intensity_seconds = Column('low_intensity_seconds', Integer())
    med_intensity_seconds = Column('med_intensity_seconds', Integer())
    high_intensity_seconds = Column('high_intensity_seconds', Integer())
    weight = Column('weight', Float())


##### Oura Tables #####
class ouraReadinessSummary(Base):
    __tablename__ = 'oura_readiness_summary'
    report_date = Column('report_date', Date(), index=True, primary_key=True)
    summary_date = Column('summary_date', Date())
    score = Column('score', Integer())
    period_id = Column('period_id', Integer())
    score_activity_balance = Column('score_activity_balance', Integer())
    score_previous_day = Column('score_previous_day', Integer())
    score_previous_night = Column('score_previous_night', Integer())
    score_recovery_index = Column('score_recovery_index', Integer())
    score_resting_hr = Column('score_resting_hr', Integer())
    score_sleep_balance = Column('score_sleep_balance', Integer())
    score_temperature = Column('score_temperature', Integer())
    score_hrv_balance = Column('score_hrv_balance', Integer())


class ouraActivitySummary(Base):
    __tablename__ = 'oura_activity_summary'
    summary_date = Column('summary_date', Date(), index=True, primary_key=True)
    average_met = Column('average_met', Float())
    cal_active = Column('cal_active', Integer())
    cal_total = Column('cal_total', Integer())
    class_5min = Column('class_5min', String(300))
    daily_movement = Column('daily_movement', Integer())
    day_end_local = Column('day_end_local', DateTime())
    day_start_local = Column('day_start_local', DateTime())
    high = Column('high', Integer())
    inactive = Column('inactive', Integer())
    inactivity_alerts = Column('inactivity_alerts', Integer())
    low = Column('low', Integer())
    medium = Column('medium', Integer())
    met_min_high = Column('met_min_high', Integer())
    met_min_inactive = Column('met_min_inactive', Integer())
    met_min_low = Column('met_min_low', Integer())
    met_min_medium = Column('met_min_medium', Integer())
    non_wear = Column('non_wear', Integer())
    rest = Column('rest', Integer())
    score = Column('score', Integer())
    score_meet_daily_targets = Column('score_meet_daily_targets', Integer())
    score_move_every_hour = Column('score_move_every_hour', Integer())
    score_recovery_time = Column('score_recovery_time', Integer())
    score_stay_active = Column('score_stay_active', Integer())
    score_training_frequency = Column('score_training_frequency', Integer())
    score_training_volume = Column('score_training_volume', Integer())
    steps = Column('steps', Integer())
    target_calories = Column('target_calories', Integer())
    timezone = Column('timezone', Integer())
    target_km = Column('target_km', Float())
    target_miles = Column('target_miles', Float())
    to_target_km = Column('to_target_km', Float())
    to_target_miles = Column('to_target_miles', Float())
    total = Column('total', Integer())


class ouraActivitySamples(Base):
    __tablename__ = 'oura_activity_samples'
    timestamp_local = Column('timestamp_local', DateTime(), index=True, primary_key=True)
    summary_date = Column('summary_date', Date())
    met_1min = Column('met_1min', Float())
    class_5min = Column('class_5min', Integer())
    class_5min_desc = Column('class_5min_desc', String(10))


class ouraSleepSummary(Base):
    __tablename__ = 'oura_sleep_summary'
    report_date = Column('report_date', Date(), index=True, primary_key=True)
    summary_date = Column('summary_date', Date())
    awake = Column('awake', Integer())
    bedtime_end_local = Column('bedtime_end_local', DateTime())
    bedtime_end_delta = Column('bedtime_end_delta', Integer())
    bedtime_start_local = Column('bedtime_start_local', DateTime())
    bedtime_start_delta = Column('bedtime_start_delta', Integer())
    breath_average = Column('breath_average', Float())
    deep = Column('deep', Integer())
    duration = Column('duration', Integer())
    efficiency = Column('efficiency', Integer())
    hr_average = Column('hr_average', Float())
    hr_lowest = Column('hr_lowest', Integer())
    hypnogram_5min = Column('hypnogram_5min', String(255))
    is_longest = Column('is_longest', Integer())
    light = Column('light', Integer())
    midpoint_at_delta = Column('midpoint_at_delta', Integer())
    midpoint_time = Column('midpoint_time', Integer())
    onset_latency = Column('onset_latency', Integer())
    period_id = Column('period_id', Integer())
    rem = Column('rem', Integer())
    restless = Column('restless', Integer())
    rmssd = Column('rmssd', Integer())
    score = Column('score', Integer())
    score_alignment = Column('score_alignment', Integer())
    score_deep = Column('score_deep', Integer())
    score_disturbances = Column('score_disturbances', Integer())
    score_efficiency = Column('score_efficiency', Integer())
    score_latency = Column('score_latency', Integer())
    score_rem = Column('score_rem', Integer())
    score_total = Column('score_total', Integer())
    temperature_delta = Column('temperature_delta', Float())
    temperature_deviation = Column('temperature_deviation', Float())
    temperature_trend_deviation = Column('temperature_trend_deviation', Float())
    timezone = Column('timezone', Integer())
    total = Column('total', Integer())


class ouraSleepSamples(Base):
    __tablename__ = 'oura_sleep_samples'
    timestamp_local = Column('timestamp_local', DateTime(), index=True, primary_key=True)
    summary_date = Column('summary_date', Date())
    report_date = Column('report_date', Date())
    rmssd_5min = Column('rmssd_5min', Integer())
    hr_5min = Column('hr_5min', Integer())
    hypnogram_5min = Column('hypnogram_5min', Integer())
    hypnogram_5min_desc = Column('hypnogram_5min_desc', String(8))


class apiTokens(Base):
    __tablename__ = 'api_tokens'
    date_utc = Column('date_utc', DateTime(), index=True, primary_key=True)
    service = Column('service', String(255))
    tokens = Column('tokens', String(255))


class dbRefreshStatus(Base):
    __tablename__ = 'db_refresh'
    timestamp_utc = Column('timestamp_utc', DateTime(), index=True, primary_key=True)
    refresh_method = Column('refresh_method', String(255))
    truncate = Column('truncate', Boolean(), default=False)
    oura_status = Column('oura_status', String(255))
    strava_status = Column('strava_status', String(255))
    withings_status = Column('withings_status', String(255))
    fitbod_status = Column('fitbod_status', String(255))


class withings(Base):
    __tablename__ = 'withings'
    date_utc = Column('date_utc', DateTime(), index=True, primary_key=True)
    weight = Column('weight', Float())
    fat_ratio = Column('fat_ratio', Float())
    hydration = Column('hydration', Float())


class fitbod(Base):
    __tablename__ = 'fitbod'
    id = Column('id', Integer(), index=True, primary_key=True, autoincrement=True)
    date_utc = Column('date_UTC', DateTime())
    exercise = Column('Exercise', String(255))
    reps = Column('Reps', Integer())
    weight = Column('Weight', Integer())
    duration = Column('Duration', Integer())
    iswarmup = Column('isWarmup', Boolean())
    note = Column('Note', String(255))


class fitbod_muscles(Base):
    __tablename__ = 'fitbod_muscles'
    exercise = Column('Exercise', String(255), index=True, primary_key=True)
    muscle = Column('Muscle', String(255))
