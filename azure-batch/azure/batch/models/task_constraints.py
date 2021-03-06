# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TaskConstraints(Model):
    """Constraints to apply to the Job Manager task.

    :param max_wall_clock_time: The maximum elapsed time that the task may
     run, measured from the time the task starts. If the task does not
     complete within the time limit, the Batch service terminates it.
    :type max_wall_clock_time: timedelta
    :param retention_time: The minimum time to retain the working directory
     for the task on the compute node where it ran, from the time it
     completes execution. After this time, the Batch service may delete the
     working directory and all its contents. The default is infinite.
    :type retention_time: timedelta
    :param max_task_retry_count: The maximum number of times the task may be
     retried. The Batch service retries a task if its exit code is nonzero.
    :type max_task_retry_count: int
    """ 

    _attribute_map = {
        'max_wall_clock_time': {'key': 'maxWallClockTime', 'type': 'duration'},
        'retention_time': {'key': 'retentionTime', 'type': 'duration'},
        'max_task_retry_count': {'key': 'maxTaskRetryCount', 'type': 'int'},
    }

    def __init__(self, max_wall_clock_time=None, retention_time=None, max_task_retry_count=None):
        self.max_wall_clock_time = max_wall_clock_time
        self.retention_time = retention_time
        self.max_task_retry_count = max_task_retry_count
