# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to get list of revisions of DOCX document
class GetListOfRevisions:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.ReviewApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source_with_revs.docx"

        revisions = api_instance.get_revisions(groupdocs_comparison_cloud.GetRevisionsRequest(source))

        print("Revisions count: " + str(len(revisions)))