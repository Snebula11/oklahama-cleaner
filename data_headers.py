mapped_data = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'district_ocd_id',
               'openstates_id', 'committee_id', 'Name', 'name_first', 'name_middle', 'name_last', 'nickname',
               'name_prefix', 'name_suffix', 'party', 'state', 'status', 'district', 'ethnicity', 'race', 'gender',
               'education', 'occupation', 'Office', 'email_official', 'email_other', 'email_campaign', 'Bio',
               'date_of_birth', 'date_of_death', 'Image', 'website_campaign', 'website_official', 'website_personal',
               'address_capitol', 'phone_capitol', 'fax_capitol', 'address_district', 'phone_district', 'fax_district',
               'contact_form_url', 'address_campaign', 'phone_campaign', 'date_assumed_office', 'appointed_by',
               'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'twitter_official',
               'twitter_personal', 'twitter_campaign', 'instagram_official', 'instagram_personal', 'instagram_campaign',
               'facebook_official', 'facebook_personal', 'facebook_campaign', 'linkedin', 'rumble', 'gab', 'RSS',
               'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id', 'ballotpedia_id', 'washington_post_id',
               'icpsr_id', 'wikipedia_id', 'google_entity_id', 'Ballotpedia URL', 'propublica URL',
               'Ballotpedia Office ID']

ballotpedia_fields = ['district_ocd_id', 'Name', 'name_first', 'name_middle', 'name_last', 'name_suffix', 'party',
                      'state', 'district', 'gender', 'Office', 'email_other', 'email_campaign', 'website_campaign',
                      'website_personal', 'address_campaign', 'phone_campaign', 'twitter_personal', 'twitter_campaign',
                      'instagram_personal', 'instagram_campaign', 'facebook_personal', 'facebook_campaign', 'linkedin',
                      'Ballotpedia URL', 'status', 'Ballotpedia Office ID']

non_bp_fields = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id', 'openstates_id', 'committee_id',
                 'nickname', 'name_prefix', 'ethnicity', 'race', 'education', 'occupation', 'email_official',
                 'Bio', 'date_of_birth', 'date_of_death', 'Image', 'website_official', 'address_capitol',
                 'phone_capitol', 'fax_capitol', 'address_district', 'phone_district', 'fax_district',
                 'contact_form_url', 'date_assumed_office', 'appointed_by', 'appointed_data', 'confirmed_date',
                 'term_end_data', 'congress_year', 'twitter_official', 'instagram_official', 'facebook_official',
                 'rumble', 'gab', 'RSS', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id',
                 'ballotpedia_id', 'washington_post_id', 'icpsr_id', 'wikipedia_id', 'google_entity_id',
                 'propublica URL']

ctcl_fields = ['state', 'Office', 'Name', 'name_first', 'name_middle', 'name_last', 'nickname', 'name_prefix',
               'name_suffix', 'party', 'phone_campaign', 'address_campaign', 'website_campaign', 'website_personal',
               'email_campaign', 'Image', 'facebook_official', 'facebook_personal', 'facebook_campaign',
               'twitter_official', 'twitter_personal', 'twitter_campaign', 'instagram_official', 'instagram_personal',
               'instagram_campaign', 'district_ocd_id', 'wikipedia_id', 'status']

non_ctcl_fields = ['govpackpub_id', 'govpack_id', 'fec_id', 'usio_id', 'opensecrets_id',
                   'openstates_id', 'committee_id', 'district', 'ethnicity', 'race', 'gender',
                   'education', 'occupation', 'email_official', 'email_other', 'Bio', 'date_of_birth', 'date_of_death',
                   'website_official', 'address_capitol', 'phone_capitol', 'fax_capitol', 'address_district',
                   'phone_district', 'fax_district', 'contact_form_url', 'date_assumed_office', 'appointed_by',
                   'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'linkedin', 'rumble', 'gab',
                   'RSS', 'thomas ID', 'lis_id', 'cspan_id', 'govtrack_id', 'votesmart_id', 'ballotpedia_id',
                   'washington_post_id', 'icpsr_id', 'google_entity_id', 'Ballotpedia URL',
                   'propublica URL', 'Ballotpedia Office ID']

incumbents_only = ['email_official', 'website_official', 'address_capitol', 'phone_capitol', 'fax_capitol',
                   'address_district', 'phone_district', 'fax_district', 'date_assumed_office', 'appointed_by',
                   'appointed_data', 'confirmed_date', 'term_end_data', 'congress_year', 'twitter_official',
                   'instagram_official', 'facebook_official']

match = False
