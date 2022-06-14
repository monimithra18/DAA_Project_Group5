#!/usr/bin/env python
# coding: utf-8

# In[4]:


def _get_score(predictions, score_team_1, score_team_2, index):
    if index == len(predictions) - 1:
        return index + 1

    if predictions[index] == '1':
        if index % 2 == 0:
            if score_team_1 + 1 > score_team_2 + (len(predictions) - index) // 2:
                return index + 1

            return _get_score(predictions, score_team_1 + 1, score_team_2, index + 1)

        if score_team_2 + 1 > score_team_1 + (len(predictions) - index) // 2:
            return index + 1

        return _get_score(predictions, score_team_1, score_team_2 + 1, index + 1)

    if predictions[index] == '0':
        if index % 2 == 0:
            if score_team_2 > score_team_1 + (len(predictions) - index - 1) // 2:
                return index + 1
        elif score_team_1 > score_team_2 + (len(predictions) - index - 1) // 2:
            return index + 1

        return _get_score(predictions, score_team_1, score_team_2, index + 1)

    if index % 2 == 0:
        if score_team_1 + 1 > score_team_2 + (len(predictions) - index) // 2:
            return index + 1

        if score_team_2 > score_team_1 + (len(predictions) - index - 1) // 2:
            return index + 1

        return min(_get_score(predictions, score_team_1 + 1, score_team_2, index + 1), _get_score(predictions, score_team_1, score_team_2, index + 1))

    if score_team_2 + 1 > score_team_1 + (len(predictions) - index) // 2:
        return index + 1

    if score_team_1 > score_team_2 + (len(predictions) - index - 1) // 2:
        return index + 1

    return min(_get_score(predictions, score_team_1, score_team_2 + 1, index + 1), _get_score(predictions, score_team_1, score_team_2, index + 1))


for _ in range(int(input())):
    predictions = input().strip()
    print(_get_score(predictions, 0, 0, 0))

