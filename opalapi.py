import json
import urllib2
import pprint

def show_c_list(candidate_list):
    # print out the list
    print("Here's your list:")
    for item in candidate_list:
         print(item)

def show_f_list(field_list):
    # print out the list
    print("Here's your list:")
    for item in field_list:
         print(item)

def add_to_list(candidate_list, new_item):
    # add new items to our list
    candidate_list.append(new_item)
        print("Added {}. List now has {} items.".format(new_item, len(candidate_list)))        
    return candidate_list

def add_to_list(field_list, new_item):
    # add new items to our list
    fields_list.append(new_item)
        print("Added {}. List now has {} items.".format(new_item, len(fields_list)))        
    return field_list

data = {
        "query" : {
                    "term" : { "name" : "sabad11214" }
                  }
}
req = urllib2.Request('http://internal-corp-UAI2005999-med-stage-708253374.us-east-1.elb.amazonaws.com/assets/elastic/search')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(data))
 
pprint.pprint(json.loads(response.read()))
