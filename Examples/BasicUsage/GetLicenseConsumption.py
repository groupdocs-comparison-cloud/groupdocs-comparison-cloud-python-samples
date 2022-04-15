# Import modules
import groupdocs_comparison_cloud
from Common import Common

#  This example demonstrates how to get metered license consumption information
class GetLicenseConsumption:
    @classmethod  
    def Run(cls):
        licenseApi = groupdocs_comparison_cloud.LicenseApi.from_config(Common.GetConfig())
        result = licenseApi.get_consumption_credit()
        print("Credits: " + str(result.credit))
        print("Quantity: " + str(result.quantity))