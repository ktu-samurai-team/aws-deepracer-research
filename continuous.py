import math


def reward_function(params):

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_location = params['objects_location']
    agent_x = params['x']
    agent_y = params['y']

    previous_object_index, next_object_index = params['closest_objects']

    if distance_from_center < 0.35 * track_width:
        reward_lane = 1.0

    elif distance_from_center < 0.5 * track_width:
        reward_lane = 3.33 * track_width - 6.66 * track_width * distance_from_center
    else:
        reward_lane = 1e-3

        next_object_loc = objects_location[next_object_index]
        previous_object_loc = objects_location[previous_object_index]

        distance_next_object = math.sqrt(
            (agent_x - next_object_loc[0])**2 + (agent_y - next_object_loc[1])**2)
        distance_previous_object = math.sqrt(
            (agent_x - previous_object_loc[0])**2 + (agent_y - previous_object_loc[1])**2)
        distance_closest_object = min(
            distance_next_object, distance_previous_object)

        if distance_closest_object < 0.25:
            reward_avoid = 1e-3
        elif 0.25 <= distance_closest_object < 0.5:
            reward_avoid = (distance_closest_object - 0.25) * 4 + 1e-3
        else:
            reward_avoid = 1.0
        return 1.0 * reward_lane + 2.0 * reward_avoid
