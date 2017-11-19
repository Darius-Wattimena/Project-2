
class GameObjectGroup:

    def __init__(self, layer):
        self.objects = []
        self.layer = layer

    def add_object(self, game_object):
        self.objects.append(game_object)

    def distance_to_above(self, current_object):
        if len(self.objects) <= 1:
            return -1
        else:
            first = True
            closest_distance = -1
            for game_object in self.objects:
                if game_object != current_object:
                    if first:
                        distance = current_object.rect.top - game_object.rect.bottom
                        if (distance >= 0):
                            closest_distance = distance
                    else:
                        distance = current_object.rect.top - game_object.rect.bottom
                        if (distance >= 0 and distance < closest_distance):
                            closest_distance = distance
            return closest_distance

    def distance_to_right(self, current_object):
        if len(self.objects <= 1):
            return -1
        else:
            first = True
            closest_distance = -1
            for game_object in self.objects:
                if game_object != current_object:
                    if first:
                        distance = current_object.rect.right - game_object.rect.left
                        if (distance >= 0):
                            closest_distance = distance
                    else:
                        distance = current_object.rect.right - game_object.rect.left
                        if (distance >= 0 and distance < closest_distance):
                            closest_distance = distance
            return closest_distance

    def distance_to_below(self, current_object):
        if len(self.objects <= 1):
            return -1
        else:
            first = True
            closest_distance = -1
            for game_object in self.objects:
                if game_object != current_object:
                    if first:
                        distance = current_object.rect.bottom - game_object.rect.top
                        if (distance >= 0):
                            closest_distance = distance
                    else:
                        distance = current_object.rect.bottom - game_object.rect.top
                        if (distance >= 0 and distance < closest_distance):
                            closest_distance = distance
            return closest_distance

    def distance_to_left(self, current_object):
        if len(self.objects <= 1):
            return -1
        else:
            first = True
            closest_distance = -1
            for game_object in self.objects:
                if game_object != current_object:
                    if first:
                        distance = current_object.rect.left - game_object.rect.right
                        if (distance >= 0):
                            closest_distance = distance
                    else:
                        distance = current_object.rect.left - game_object.rect.right
                        if (distance >= 0 and distance < closest_distance):
                            closest_distance = distance
            return closest_distance