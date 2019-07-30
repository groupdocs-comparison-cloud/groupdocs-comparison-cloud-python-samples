# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Object_Exists:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_StorageApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.ObjectExistsRequest("comparisondocs\\one-page.docx", Common_Utilities.myStorage)
            response = api.object_exists(request)
            
            print("Expected response type is ObjectExist: " + str(response))
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))