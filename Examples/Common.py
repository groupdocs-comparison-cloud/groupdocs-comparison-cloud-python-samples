import groupdocs_comparison_cloud
import glob
import os

class Common:

    # This properties are set from main class
    app_sid = None
    app_key = None
    myStorage = None
    
    @classmethod  
    def GetConfig(cls):
        configuration = groupdocs_comparison_cloud.Configuration(cls.app_sid, cls.app_key)
        configuration.api_base_url = "https://api.groupdocs.cloud"
        return configuration

    @classmethod  
    def UploadSampleFiles(cls):
        
        # api initialization
        storageApi = groupdocs_comparison_cloud.StorageApi.from_config(cls.GetConfig())
        fileApi = groupdocs_comparison_cloud.FileApi.from_config(cls.GetConfig())

        # upload sample files
        for filename in glob.iglob("Resources/**/*.*", recursive=True):
            destFile = filename.replace("Resources\\", "", 1)            
            fileExistsResponse = storageApi.object_exists(groupdocs_comparison_cloud.ObjectExistsRequest(destFile))
            if not fileExistsResponse.exists:                                
                fileApi.upload_file(groupdocs_comparison_cloud.UploadFileRequest(destFile, filename))
                print("Uploaded file: "+ destFile)
