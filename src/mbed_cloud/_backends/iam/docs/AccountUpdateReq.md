# AccountUpdateReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line2** | **str** | Postal address line 2, not longer than 100 characters. | [optional] 
**city** | **str** | The city part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**address_line1** | **str** | Postal address line 1, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**display_name** | **str** | The display name for the account, not longer than 100 characters. | [optional] 
**mfa_status** | **str** | The enforcement status of setting up the multi-factor authentication. &#39;Enforced&#39; means that setting up the MFA is required after login. &#39;Optional&#39; means that the MFA is not required. | [optional] 
**country** | **str** | The country part of the postal address, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**company** | **str** | The name of the company, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**idle_timeout** | **str** | The reference token expiration time in minutes for this account. Between 1 and 120 minutes. | [optional] 
**notification_emails** | **list[str]** | A list of notification email addresses. | [optional] 
**state** | **str** | The state part of the postal address, not longer than 100 characters. | [optional] 
**contact** | **str** | The name of the contact person for this account, not longer than 100 characters. Required for commercial accounts only. | [optional] 
**postal_code** | **str** | The postal code part of the postal address, not longer than 100 characters. | [optional] 
**account_properties** | [**dict(str, dict(str, str))**](dict.md) | Properties for this account. | [optional] 
**expiration_warning_threshold** | **str** | Indicates how many days before account expiration a notification email should be sent. Valid values are: 1-180. | [optional] 
**password_policy** | [**PasswordPolicy**](PasswordPolicy.md) | Password policy for this account. | [optional] 
**end_market** | **str** | The end market for this account, not longer than 100 characters. | [optional] 
**phone_number** | **str** | The phone number of a representative of the company, not longer than 100 characters. | [optional] 
**email** | **str** | The company email address for this account, not longer than 254 characters. Required for commercial accounts only. | [optional] 
**aliases** | **list[str]** | An array of aliases, not more than 10. An alias is not shorter than 8 and not longer than 100 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


