mapped_data = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'district_ocd_id',
               'openstates_id', 'committee_id', 'name', 'name_first', 'name_middle', 'name_last', 'nickname',
               'name_prefix', 'name_suffix', 'title', 'party', 'state', 'status', 'district', 'ethnicity', 'race',
               'gender', 'education', 'occupation', 'Office', 'email_official', 'email_other', 'email_campaign', 'Bio',
               'date_of_birth', 'date_of_death', 'Image', 'website_campaign', 'website_official', 'website_personal',
               'address_capitol', 'phone_capitol', 'fax_capitol', 'address_district', 'phone_district', 'fax_district',
               'contact_form_url', 'address_campaign', 'phone_campaign', 'date_assumed_office', 'appointed_by',
               'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'twitter_official',
               'twitter_personal', 'twitter_campaign', 'youtube_official', 'youtube_personal', 'youtube_campaign',
               'instagram_official', 'instagram_personal', 'instagram_campaign', 'facebook_official',
               'facebook_personal', 'facebook_campaign', 'linkedin', 'rumble', 'gab', 'RSS', 'thomas ID', 'lis_id',
               'cspan_id', 'govtrack_id', 'votesmart_id', 'ballotpedia_id', 'washington_post_id', 'icpsr_id',
               'wikipedia_id', 'google_entity_id', 'Ballotpedia URL', 'propublica URL', 'Ballotpedia Office ID']

new_column_headers = ['name', 'name_first', 'name_middle', 'name_last', 'nickname', 'name_prefix', 'name_suffix',
                      'Image', 'party', 'Office', 'title', 'state', 'status', 'district', 'ethnicity', 'race', 'gender',
                      'date_of_birth', 'date_of_death', 'education', 'occupation', 'Bio', 'email_official',
                      'email_other', 'email_campaign', 'website_official', 'website_personal', 'website_campaign',
                      'twitter_official', 'twitter_personal', 'twitter_campaign', 'youtube_official',
                      'youtube_personal', 'youtube_campaign', 'instagram_official', 'instagram_personal',
                      'instagram_campaign', 'facebook_official', 'facebook_personal', 'facebook_campaign', 'linkedin',
                      'rumble', 'gab', 'RSS', 'address_campaign', 'address_capitol', 'address_district',
                      'phone_campaign', 'phone_capitol', 'phone_district', 'fax_capitol', 'fax_district',
                      'contact_form_url', 'date_assumed_office', 'appointed_by', 'appointed_data', 'confirmed_date',
                      'term_end_data', 'congress_year', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id',
                      'votesmart_id', 'ballotpedia_id', 'washington_post_id', 'icpsr_id', 'wikipedia_id',
                      'google_entity_id', 'Ballotpedia URL', 'propublica URL', 'Ballotpedia Office ID', 'govpackpub_id',
                      'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'district_ocd_id', 'openstates_id',
                      'committee_id']

ballotpedia_fields = ['district_ocd_id', 'name', 'name_first', 'name_middle', 'name_last', 'name_suffix', 'party',
                      'state', 'district', 'gender', 'Office', 'email_other', 'email_campaign', 'website_campaign',
                      'website_personal', 'address_campaign', 'phone_campaign', 'twitter_personal', 'twitter_campaign',
                      'instagram_personal', 'instagram_campaign', 'facebook_personal', 'facebook_campaign', 'linkedin',
                      'Ballotpedia URL', 'status', 'Ballotpedia Office ID', 'youtube_personal', 'youtube_campaign']

non_bp_fields = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'openstates_id', 'committee_id',
                 'nickname', 'name_prefix', 'ethnicity', 'race', 'education', 'occupation', 'email_official',
                 'Bio', 'date_of_birth', 'date_of_death', 'Image', 'website_official', 'address_capitol',
                 'phone_capitol', 'fax_capitol', 'address_district', 'phone_district', 'fax_district',
                 'contact_form_url', 'date_assumed_office', 'appointed_by', 'appointed_data', 'confirmed_date',
                 'term_end_data', 'congress_year', 'twitter_official', 'instagram_official', 'facebook_official',
                 'rumble', 'gab', 'RSS', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id',
                 'ballotpedia_id', 'washington_post_id', 'icpsr_id', 'wikipedia_id', 'google_entity_id',
                 'propublica URL', 'youtube_official']

openstates_data = ['openstates_id', 'name', 'name_first', 'name_middle', 'name_last', 'nickname', 'name_suffix',
                   'party', 'district', 'Office', 'gender', 'email_official', 'Bio', 'date_of_birth', 'date_of_death',
                   'Image', 'status', 'address_capitol', 'phone_capitol', 'fax_capitol', 'address_district',
                   'phone_district', 'fax_district', 'youtube_campaign', 'twitter_campaign', 'instagram_campaign',
                   'facebook_campaign']

non_openstates_data = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'district_ocd_id',
                       'committee_id', 'name_prefix', 'state', 'ethnicity', 'race', 'education', 'occupation',
                       'email_other', 'email_campaign', 'website_campaign', 'website_official', 'website_personal',
                       'contact_form_url', 'address_campaign', 'phone_campaign', 'date_assumed_office', 'appointed_by',
                       'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'twitter_official',
                       'twitter_personal', 'youtube_official', 'youtube_personal', 'instagram_official',
                       'instagram_personal', 'facebook_official', 'facebook_personal', 'linkedin', 'rumble', 'gab',
                       'RSS', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id', 'ballotpedia_id',
                       'washington_post_id', 'icpsr_id', 'wikipedia_id', 'google_entity_id', 'Ballotpedia URL',
                       'propublica URL', 'Ballotpedia Office ID']

ctcl_fields = ['state', 'Office', 'name', 'name_first', 'name_middle', 'name_last', 'nickname', 'name_prefix',
               'name_suffix', 'party', 'phone_campaign', 'address_campaign', 'website_campaign', 'website_personal',
               'email_campaign', 'Image', 'facebook_official', 'facebook_personal', 'facebook_campaign',
               'twitter_official', 'twitter_personal', 'twitter_campaign', 'instagram_official', 'instagram_personal',
               'instagram_campaign', 'district_ocd_id', 'wikipedia_id', 'status', 'youtube_official',
               'youtube_personal', 'youtube_campaign']

non_ctcl_fields = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id',
                   'openstates_id', 'committee_id', 'district', 'ethnicity', 'race', 'gender',
                   'education', 'occupation', 'email_official', 'email_other', 'Bio', 'date_of_birth', 'date_of_death',
                   'website_official', 'address_capitol', 'phone_capitol', 'fax_capitol', 'address_district',
                   'phone_district', 'fax_district', 'contact_form_url', 'date_assumed_office', 'appointed_by',
                   'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'linkedin', 'rumble', 'gab',
                   'RSS', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id', 'ballotpedia_id',
                   'washington_post_id', 'icpsr_id', 'google_entity_id', 'Ballotpedia URL',
                   'propublica URL', 'Ballotpedia Office ID']

propublica_fields = ['name', 'name_first', 'name_middle', 'name_last', 'name_suffix', 'date_of_birth', 'propublica URL',
                     'gender', 'youtube_official', 'twitter_official', 'facebook_official', 'cspan_id', 'govtrack_id',
                     'votesmart_id', 'icpsr_id', 'google_entity_id', 'fec_id', 'RSS', 'website_official', 'status',
                     'district_ocd_id', 'address_capitol', 'phone_capitol', 'fax_capitol', 'state', 'party', 'district',
                     'Office', 'lis_id']

non_propublica_fields = ['govpackpub_id', 'govpack_id', 'usio_id', 'opensecrets_id', 'openstates_id',
                         'committee_id', 'nickname', 'name_prefix', 'ethnicity',
                         'race', 'education', 'occupation', 'email_official', 'email_other', 'email_campaign',
                         'Bio', 'date_of_death', 'Image', 'website_campaign', 'website_personal', 'address_district',
                         'phone_district', 'fax_district',
                         'address_campaign', 'phone_campaign', 'date_assumed_office', 'appointed_by', 'appointed_data',
                         'confirmed_date', 'term_end_data', 'congress_year', 'twitter_personal', 'twitter_campaign',
                         'youtube_personal', 'youtube_campaign', 'instagram_official', 'instagram_personal',
                         'instagram_campaign', 'facebook_personal', 'facebook_campaign', 'linkedin', 'rumble', 'gab',
                         'thomas ID', 'ballotpedia_id', 'washington_post_id', 'wikipedia_id',
                         'Ballotpedia URL', 'Ballotpedia Office ID']

incumbents_only = ['email_official', 'website_official', 'address_capitol', 'phone_capitol', 'fax_capitol',
                   'address_district', 'phone_district', 'fax_district', 'date_assumed_office', 'appointed_by',
                   'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'twitter_official',
                   'instagram_official', 'facebook_official', 'youtube_official']

suffixes = ['Jr.', 'Sr.', 'M.D.', 'Ph.D.', 'I', 'II', 'III', 'IV', 'V']
