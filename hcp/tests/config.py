# Author: Denis A. Engemann <denis.engemann@gmail.com>
# License: BSD (3-clause)

import os
import os.path as op
from ..io.file_mapping import get_s3_keys_anatomy, get_s3_keys_meg


hcp_prefix = 's3://hcp-openaccess/HCP_900'
subject = '105923'


hcp_data_types = [
    'rest',
    'task_working_memory',
    'task_story_math',
    'task_motor',
    'noise_empty_room'
]

hcp_outputs = [
    'raw',
    'epochs',
    'ica',
    'evoked',
    'trial_info',
    'bads'
]

hcp_onsets = ['stim']

# allow for downloading fewer data
run_inds = [0, 1, 2][:int(os.getenv('MNE_HCP_N_RUNS', 3))]

s3_keys = list()

s3_keys += get_s3_keys_anatomy(
    subject, hcp_path_bucket=hcp_prefix, mode='minimal')

s3_keys += get_s3_keys_meg(
    subject, data_types=[
        k for k in hcp_data_types if 'noise' not in k],
    onsets=hcp_onsets,
    hcp_path_bucket=hcp_prefix,
    outputs=hcp_outputs, run_inds=run_inds)

##############################################################################
# variable used in different tests

hcp_path = op.join(op.expanduser('~'), 'mne-hcp-data', 'HCP')

bti_chans = {'A' + str(i) for i in range(1, 249, 1)}

test_subject = '105923'
task_types = ['task_story_math', 'task_working_memory', 'task_motor']
noise_types = ['noise_empty_room']
sfreq_preproc = 508.63
sfreq_raw = 2034.5101
lowpass_preproc = 150
highpass_preproc = 1.3

epochs_bounds = {
    'task_motor': (-1.2, 1.2),
    'task_working_memory': (-1.5, 2.5),
    'task_story_math': (-1.5, 4),
    'rest': (0, 2)
}
