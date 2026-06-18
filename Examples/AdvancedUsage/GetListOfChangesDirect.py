# Import modules
import os
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to get list of changes by sending documents directly as multipart/form-data,
# without pre-uploading them to cloud storage.
class GetListOfChangesDirect:
    @classmethod
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.CompareApi.from_config(Common.GetConfig())

        source_path = os.path.join("Resources", "source_files", "word", "source.docx")
        target_path = os.path.join("Resources", "target_files", "word", "target.docx")

        request = groupdocs_comparison_cloud.PutChangesRequest(source_path, [target_path])

        changes = api_instance.put_changes(request)

        print("Changes count: " + str(len(changes)))
