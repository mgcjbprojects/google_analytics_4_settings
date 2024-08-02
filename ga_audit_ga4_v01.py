# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:26:40 2024

@author: Maria Colmenarez
"""
###Libraries###

import pandas as pd
from google.oauth2 import service_account
from google.analytics.admin_v1alpha import AnalyticsAdminServiceClient, ListAccountSummariesRequest, GetAccountRequest, ListGoogleAdsLinksRequest, GetDataRetentionSettingsRequest, GetDataSharingSettingsRequest, GetGoogleSignalsSettingsRequest, GetEnhancedMeasurementSettingsRequest,GetAttributionSettingsRequest, ListMeasurementProtocolSecretsRequest, ListDataStreamsRequest, ListPropertiesRequest, ListSearchAds360LinksRequest,ListCustomDimensionsRequest, ListCustomMetricsRequest, ListBigQueryLinksRequest,ListAdSenseLinksRequest 
import xlsxwriter   

#pip install xlsxwriter if is not installed

###  Set up credentials and variables for your account_id, property_id, stream_id //IMPORTANT: THIS ONLY WORKS FOR 1 PROPERTY WITH ONE DATA STREAM ###

credentials = service_account.Credentials.from_service_account_file('ga4-audit-417301-857701afdbce.json')

account_id = "199113898"

property_id = "275233208"

stream_id = "2644899550"

###Create an Analytics Admin Service client###
client = AnalyticsAdminServiceClient(credentials=credentials)

### 1. For account###

# Create empty list
account_data = []

# Run function

def get_account(account_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results = client.get_account(name=f'accounts/{account_id}')


  # Extract data from the single Account object
account_data = {
    "name": results.name,
    "display_name": results.display_name,
    "region_code": results.region_code,
    "acc_create_time": results.create_time.timestamp()
  }
 
# Print the results (optional)
print(account_data)

# Convert list in dataframe 

df_account = pd.DataFrame(account_data, index=range(1))  # Adjust range as needed



### 2. For property data ###

# Create empty list
property_data = []


# Run function

def list_property(account_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
request= ListPropertiesRequest(filter=f'parent:accounts/{account_id}')
page_result= client.list_properties(request=request)
   # Loop for properties
for response in page_result:
        print(response)  
        property_data.append({
       "property_name": response.name,
       "property_type": response.property_type.name,
       "property_display_name": response.display_name,
       "property_industry_category": response.industry_category.name,
       "property_time_zone": response.time_zone,
       "property_currency_code": response.currency_code,
       "property_service_level": response.service_level.name,
       "parent_account":response.account,
       "property_created_time":response.create_time.timestamp()
       
       # Add other properties you want to include
          })
        
 # Convert list in dataframe      
df_property = pd.DataFrame(property_data)  

### 3. For data streams ###

# Create empty list
streams_data = []

# Run function

def list_data_streams(property_id: str, transport: str = None):
  """
  Lists data streams
  """
  # Retrieve account information
request2 = ListDataStreamsRequest(parent=f'properties/{property_id}')
page_result2 = client.list_data_streams(request=request2)
   # Loop for properties
for response2 in page_result2:
        print(response2)

        streams_data.append({
       "streams_name": response2.name,
       "streams_type": response2.type.name,
       "streams_display_name": response2.display_name,
       "streams_created_time":response.create_time.timestamp()
       
       # Add other properties you want to include
          })
        
 # Convert list in dataframe      
df_streams = pd.DataFrame(streams_data)  



### 4. For data retention settings: property view ###


# Create empty list
retention_data = []

# Run function

def get_data_retention_settings(property_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results2 = client.get_data_retention_settings(name=f'properties/{property_id}/dataRetentionSettings')

print(results2)
  # Extract data from the single Account object
retention_data = {
    "retention_name": results2.name,
    "event_data_retention": results2.event_data_retention.name,
    "reset_user_data_on_new_activity": results2.reset_user_data_on_new_activity
  }
 
# Print the results (optional)
print(retention_data)

# Convert list in dataframe 

df_retention = pd.DataFrame(retention_data, index=range(1))  # Adjust range as needed




### 5. For data retention settings: account view ###


# Create empty list
sharing_data = []

# Run function

def get_data_sharing_settings(account_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results3 = client.get_data_sharing_settings(name=f'accounts/{account_id}/dataSharingSettings')

print(results3)
  # Extract data from the single Account object
sharing_data = {
    "sharing_name": results3.name,
    "sharing_with_google_support_enabled": results3.sharing_with_google_support_enabled,
    "sharing_with_google_assigned_sales_enabled": results3.sharing_with_google_any_sales_enabled,
    "sharing_with_google_products_enabled": results3.sharing_with_google_products_enabled,
    "sharing_with_others_enabled": results3.sharing_with_others_enabled,   
  }
 
# Print the results (optional)
print(sharing_data)

# Convert list in dataframe 

df_sharing = pd.DataFrame(sharing_data , index=range(1))  # Adjust range as needed



### 6. For Google Signals settings: property view ###


# Create empty list
signals_data = []

# Run function

def get_google_signals_settings(property_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results4 = client.get_google_signals_settings(name=f'properties/{property_id}/googleSignalsSettings')

print(results4)
  # Extract data from the single Account object
signals_data  = {
    "signals_name": results4.name,
    "signals_state": results4.state.name,
    "signals_consent": results4.consent.name 
  }
 
# Print the results (optional)
print(signals_data)

# Convert list in dataframe 

df_signals = pd.DataFrame(signals_data, index=range(1))  # Adjust range as needed



### 7. For Attribution Settings: property view ###


# Create empty list
attribution_data = []

# Run function

def get_attribution_settings(property_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results5 = client.get_attribution_settings(name=f'properties/{property_id}/attributionSettings')

print(results5)
  # Extract data from the single Account object
attribution_data = {
    "attribution_name": results4.name,
    "acquisition_conversion_event_lookback_window": results5.acquisition_conversion_event_lookback_window.name,
    "other_conversion_event_lookback_window": results5.other_conversion_event_lookback_window.name,
    "reporting_attribution_model": results5.reporting_attribution_model.name,
    "ads_web_conversion_data_export_scope": results5.ads_web_conversion_data_export_scope.name,
  }
 
# Print the results (optional)
print(attribution_data)

# Convert list in dataframe 

df_attribution = pd.DataFrame(attribution_data, index=range(1))  # Adjust range as needed



### 8. For MeasurementProtocolSecretRequest: property view ###


# Create empty list
measurement_data = []

# Run function
def list_measurement_protocol_secrets(property_id: str, stream_id: str, transport: str = None):
  """
  Lists measurement protocol secrets for a data stream.
  """

  # Retrieve measurement protocol secrets using the API
  request3 = ListMeasurementProtocolSecretsRequest(parent=f'properties/{property_id}/dataStreams/{stream_id}')
  try:
    page_result3 = client.list_measurement_protocol_secrets(request=request3)
  except HttpError as error:
    print(f"An HTTP error {error.http_error_status_code} occurred: {error.message}")
    return measurement_data  # Return the empty list on error


  # Loop through the results, handling potential missing responses
  for response3 in page_result3.yield_from():
    if hasattr(response3, 'secret'):  # Check for 'secret' existence
      # Extract the secret value (or set to 0 if missing)
      secret_value = response3.secret.secret_value or 0
      measurement_data.append(secret_value)
    else:
      # Add 0 if there's no secret in this response
      measurement_data.append(0)

  return measurement_data


### 9. For GetEnhancedMeasurementSettingsRequest: measurement view ###


# Create empty list
enhanced_data = []

# Run function

def get_enhanced_measurement_settings(property_id: str, stream_id: str, transport: str = None):
  """
  Lists summary account
  """
  # Retrieve account information
results6 = client.get_enhanced_measurement_settings(name=f'properties/{property_id}/dataStreams/{stream_id}/enhancedMeasurementSettings')

print(results6)
  # Extract data from the single Account object
enhanced_data = {
    "enhanced_name": results6.name,
    "outbound_clicks_enabled": results6.outbound_clicks_enabled,
    "other_conversion_event_lookback_window": results5.other_conversion_event_lookback_window.name,
    "site_search_enabled": results6.site_search_enabled,
    "page_changes_enabled": results6.page_changes_enabled,
  }
 
# Print the results (optional)
print(enhanced_data)

# Convert list in dataframe 

df_enhanced = pd.DataFrame(enhanced_data, index=range(1))  # Adjust range as needed


### 10. For ListCustomDimensionsRequest,: measurement view ###

# Initialize an empty list outside the try block
customdim_data = []

def list_custom_dimensions(property_id: str, transport: str = None):
    """
    Lists data streams
    """
    try:
        # Retrieve account information
        request4 = ListCustomDimensionsRequest(parent=f'properties/{property_id}')
        page_result4 = client.list_custom_dimensions(request=request4)
        # Loop for properties
        for response4 in page_result4:
            print(response4)
            
            customdim_data.append({
                "customdim_name": response4.name,
                "customdim_display_name": response4.display_name,
                "customdim_parameter_name": response4.parameter_name,
                "customdim_scope": response4.scope.name     
                # Add other properties you want to include
            })
    
    # Handle errors if the property doesn't have custom dimensions
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return an empty list if an error occurs
        return customdim_data
    
   
    
# Example usage
custom_dimensions = list_custom_dimensions(f'{property_id}')
print(custom_dimensions)

df_customdim = pd.DataFrame(customdim_data)



### 11. For ListCustomMetricsRequest,: measurement view ###

# Initialize an empty list outside the try block
customet_data = []

def  list_custom_metrics(property_id: str, transport: str = None):
    """
    Lists data streams
    """
    try:
        # Retrieve account information
        request5 = ListCustomMetricsRequest(parent=f'properties/{property_id}')
        page_result5 = client.list_custom_metrics(request=request5)
        # Loop for properties
        for response5 in page_result5:
            print(response5)
            
            customet_data.append({
                " customet_name": response5.name,
                " customet_display_name": response5.display_name,
                " customet_parameter_name": response5.parameter_name,
                " customet_scope": response5.scope.name     
                # Add other properties you want to include
            })
    
    # Handle errors if the property doesn't have custom dimensions
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return an empty list if an error occurs
        return customet_data
      
# Example usage
custom_metrics= list_custom_metrics(f'{property_id}')
print(custom_metrics)

df_customet = pd.DataFrame(customet_data)




### 12. For ListGoogleAdsLinksRequest: integrations view ###

# Initialize an empty list outside the try block
ads_links_data = []

def  list_google_ads_links(property_id: str, transport: str = None):
    """
    Lists data streams
    """
    try:
    # Retrieve account information
      request6 =  ListGoogleAdsLinksRequest(parent=f'properties/{property_id}')
      page_result6 = client. list_google_ads_links(request=request6)
# Loop for properties

      for response6 in page_result6:
        print(response6)
        
        ads_links_data.append({
            " ads_links_name": response6.name,
            " ads_links_customer_id": response6.customer_id,
            " ads_links_created_time": response6.create_time.timestamp(),
            " ads_personalization_enabled": response6.ads_personalization_enabled
            # Add other properties you want to include
        })

    # Handle errors if the property doesn't have custom dimensions
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return an empty list if an error occurs
        return ads_links_data
      

# Example usage
google_ad_links= list_google_ads_links(f'{property_id}')
print(google_ad_links)

df_adlinks = pd.DataFrame(ads_links_data)

### 13. For ListBigQueryLinksRequest: integrations view ###

# Initialize an empty list outside the try block
bq_links_data = []

def  list_big_query_links(property_id: str, transport: str = None):
    """
    Lists data streams
    """
    try:
    # Retrieve account information
      request7 =  ListBigQueryLinksRequest(parent=f'properties/{property_id}')
      page_result7 = client.list_big_query_links(request=request7)
# Loop for properties

      for response7 in page_result7:
        print(response7)
        
        bq_links_data.append({
            " bq_links_name": response7.name,
            " bq_links_project": response7.project,
            " bq_links_create_time": response7.create_time.timestamp(),
            " bq_links_daily_export_enabled": response7.daily_export_enabled,
            # Add other properties you want to include
        })

    # Handle errors if the property doesn't have custom dimensions
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return an empty list if an error occurs
        return bq_links_data
      

# Example usage
bq_links= list_big_query_links(f'{property_id}')
print(list_big_query_links)

df_bqlinks = pd.DataFrame(bq_links_data)



### UNIR DATAFRAMES###

#FOR ACCOUNT

df1 = pd.concat([df_account,df_sharing], axis=1)
#FOR PROPERTY
df2 = pd.concat([df_property,df_retention, df_signals, df_attribution], axis=1)


### EXPORTAR A EXCEL#
writer = pd.ExcelWriter("ga4_audit.xlsx", engine="xlsxwriter")
df1.to_excel(writer, sheet_name='Account')
df2.to_excel(writer, sheet_name='Properties')
df_enhanced.to_excel(writer, sheet_name='Measurement')
df_customdim.to_excel(writer, sheet_name='Custom_dimensions')
df_customet.to_excel(writer, sheet_name='Custom_metrics')
df_adlinks.to_excel(writer, sheet_name='Google_Ads_Links')
df_bqlinks.to_excel(writer, sheet_name='Google_BQ_Links')
writer.close()








