#IO
#INPUT_DIR='/home/srihari/Desktop/anuvaad-toolkit/t3'
#OUTPUT_DIR='/home/srihari/Desktop/anuvaad-toolkit/outputs'

#INPUT_DIR='/home/dhiraj/Documents/Anuwad/AIB/ta_set_1'
#OUTPUT_DIR='/home/dhiraj/Documents/Anuwad/AIB/ta_set_1'

INPUT_DIR='/home/sujit27/projects/audio-to-text/testing_bn/transcription'
OUTPUT_DIR='/home/sujit27/projects/audio-to-text/testing_bn/transcription'


#INPUT_DIR='/home/dhiraj/Documents/Anuwad/AIB/test_large'
#OUTPUT_DIR='/home/dhiraj/Documents/Anuwad/AIB/test_large'
BATCH_SIZE=1
#LOGS='ocr_tok_stage_p3.log'
LOGS='ocr_tok_new_stage.log'

SAVE_JSON=True
OVERWRITE=False

#LOGIN DEV
# LOGIN='https://auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login'
# USER="dhiraj.daga@tarento.com"
# PASS="Cv@123"

#LOGIN STAGE
LOGIN='https://stage-auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login'
USER="stageuser@tarento.com"
PASS="Welcome@123"


#WF CONFIG DEV
# WF_INIT= "https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/async/initiate"
# WF_CODE  = "WF_A_FCWDLDBSOD15GVOTK"
# SEARCH='https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk'
# DOWNLOAD="https://auth.anuvaad.org/download/"
# UPLOAD='https://auth.anuvaad.org/anuvaad-api/file-uploader/v0/upload-file'

#WF CONFIG STAGE
WF_INIT= "https://stage-auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/async/initiate"
WF_CODE  = "WF_A_FCWDLDBSOD15GVOTK"
SEARCH='https://stage-auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk'
DOWNLOAD="https://stage-auth.anuvaad.org/download/"
UPLOAD='https://stage-auth.anuvaad.org/anuvaad-api/file-uploader/v0/upload-file'





# #IO
# INPUT_DIR='/home/srihari/Desktop/anuvaad-toolkit/input'
# OUTPUT_DIR='/home/srihari/Desktop/anuvaad-toolkit/outputs'
# #INPUT_DIR='/home/dhiraj/Documents/benchmark/t1'
# #OUTPUT_DIR='/home/dhiraj/Documents/benchmark/t1'

# BATCH_SIZE=6
# LOGS='ocr_tok.log'
# SAVE_JSON=True
# OVERWRITE=False

# #LOGIN DEV
# LOGIN='https://auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login'
# USER="dhiraj.daga@tarento.com"
# PASS="Cv@123"

# #LOGIN STAGE
# # LOGIN='https://stage-auth.anuvaad.org/anuvaad/user-mgmt/v1/users/login'
# # USER="stageuser@tarento.com"
# # PASS="Welcome@123"


# #WF CONFIG DEV
# WF_INIT= "https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/async/initiate"
# WF_CODE  = "WF_A_FCWDLDBSOD15GVOTK"
# SEARCH='https://auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk'
# DOWNLOAD="https://auth.anuvaad.org/download/"
# UPLOAD='https://auth.anuvaad.org/anuvaad-api/file-uploader/v0/upload-file'

# #WF CONFIG STAGE
# # WF_INIT= "https://stage-auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/async/initiate"
# # WF_CODE  = "WF_A_FCWDLDBSOD15GVOTK"
# # SEARCH='https://stage-auth.anuvaad.org/anuvaad-etl/wf-manager/v1/workflow/jobs/search/bulk'
# # DOWNLOAD="https://stage-auth.anuvaad.org/download/"
# # UPLOAD='https://stage-auth.anuvaad.org/anuvaad-api/file-uploader/v0/upload-file'




