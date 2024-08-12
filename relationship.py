from graph import DG
import json

family_relationship = {
    "sibling": ["sister", "brother"],
    "SO": ["wife", "husband"],
    "child": ["daughter", "son"],
    "inv-child": ["mother", "father"],
    "grand": ["granddaughter", "grandson"],
    "inv-grand": ["grandmother", "grandfather"],
    "un": ["niece", "nephew"],
    "inv-un": ["aunt", "uncle"],
    "in-law": ["daughter-in-law", "son-in-law"],
    "inv-in-law": ["mother-in-law", "father-in-law"],
}

def general_rules(remove_nodes=None):
    rules = []
    for node in (DG.nodes):
        if node in list(range(1, 17)):
            predecessor_2 = None 
            if len(list(DG.predecessors(node))) == 1:
                predecessor_2 = list(DG.predecessors(node))[0]
            else:
                predecessor_2 = list(DG.predecessors(node))[1]    
            rule = {
                "successor": list(DG.successors(node))[0],
                "predecessor_1": list(DG.predecessors(node))[0],
                "predecessor_2": predecessor_2,
            }
            rules.append(rule)
    return rules

def specific_rules(rules):
    ground_rules = []
    for rule in rules:
        for i in range(0,2):
            for j in range(0,2):
                successor = family_relationship[rule["successor"]][i]
                ground_rule = {
                    "successor" : family_relationship[rule["successor"]][i],
                    "predecessor_1" : family_relationship[rule["predecessor_1"]][j],
                    "predecessor_2" : family_relationship[rule["predecessor_2"]][i],
                }
                ground_rules.append(ground_rule)
    return ground_rules

print(specific_rules(general_rules()))

#convert the rules to json file
with open("rules.json", "w") as f:
    json.dump(specific_rules(general_rules()), f, indent=4)

#convert the rules to asp
def convert_to_asp_rule(rule):
    successor = rule["successor"]
    predecessor_1 = rule["predecessor_1"]
    predecessor_2 = rule["predecessor_2"]
    
    asp_rule = f"{successor}(A, C) :- {predecessor_1}(A, B), {predecessor_2}(B, C)."
    return asp_rule

def all_asp_rules(rules):
    asp_rules = ""
    for rule in rules:
        asp_rules += convert_to_asp_rule(rule) + "\n" 
    return asp_rules

#convert asp to rules
def convert_to_rule(asp_rule):
    asp_rule = asp_rule.replace(":-", "").replace("(", " ").replace(")", "").replace(",", "").replace(".", "")
    asp_rule = asp_rule.split(" ")
    rule = {
        "successor": asp_rule[0],
        "predecessor_1": asp_rule[4],
        "predecessor_2": asp_rule[7]
    }
    return rule

def check_rule_valid(gen_rule, foundation_rules):
    for rule in foundation_rules:
        if gen_rule["successor"] != rule["successor"] and gen_rule["predecessor_1"] == rule["predecessor_1"] and gen_rule["predecessor_2"] == rule["predecessor_2"]:
            return False
    return True

print(check_rule_valid({"successor": "sister", "predecessor_1": "daughter", "predecessor_2": "son"}, specific_rules(general_rules())))






