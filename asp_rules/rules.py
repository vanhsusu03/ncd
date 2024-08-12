rules = '''
% Rule 1
son(A, C) :- son(A, B), brother(B, C).
% Rule 2
daughter(A, C) :- daughter(A, B), sister(B, C).
% Rule 3
daughter(A, C) :- son(A, B), sister(B, C).
% Rule 4
son(A, C) :- daughter(A, B), brother(B, C).
% Rule 5
sister(A, C) :- sister(A, B), sister(B, C).
% Rule 6
brother(A, C) :- sister(A, B), brother(B, C).
% Rule 7
sister(A, C) :- daughter(A, B), aunt(B, C).
% Rule 8
brother(A, C) :- daughter(A, B), uncle(B, C).
% Rule 9
brother(A, C) :- son(A, B), uncle(B, C).
% Rule 10
brother(A, C) :- brother(A, B), brother(B, C).
% Rule 11
sister(A, C) :- father(A, B), daughter(B, C).
% Rule 12
brother(A, C) :- mother(A, B), son(B, C).
% Rule 13
brother(A, C) :- father(A, B), son(B, C).
% Rule 14
sister(A, C) :- mother(A, B), daughter(B, C).
% Rule 15
father(A, C) :- brother(A, B), father(B, C).
% Rule 16
sister(A, C) :- brother(A, B), sister(B, C).
% Rule 17
sister(A, C) :- son(A, B), aunt(B, C).
% Rule 18
mother(A, C) :- brother(A, B), mother(B, C).
% Rule 19
father(A, C) :- sister(A, B), father(B, C).
% Rule 20
mother(A, C) :- sister(A, B), mother(B, C).
% Rule 21
aunt(A, C) :- mother(A, B), sister(B, C).
% Rule 22
uncle(A, C) :- father(A, B), brother(B, C).
% Rule 23
father(A, C) :- daughter(A, B), grandfather(B, C).
% Rule 24
aunt(A, C) :- father(A, B), sister(B, C).
% Rule 25
uncle(A, C) :- mother(A, B), brother(B, C).
% Rule 26
daughter(A, C) :- husband(A, B), daughter(B, C).
% Rule 27
son(A, C) :- wife(A, B), son(B, C).
% Rule 28
son(A, C) :- husband(A, B), son(B, C).
% Rule 29
father(A, C) :- son(A, B), grandfather(B, C).
% Rule 30
niece(A, C) :- brother(A, B), daughter(B, C).
% Rule 31
niece(A, C) :- sister(A, B), daughter(B, C).
% Rule 32
nephew(A, C) :- sister(A, B), son(B, C).
% Rule 33
nephew(A, C) :- brother(A, B), son(B, C).
% Rule 34
daughter(A, C) :- wife(A, B), daughter(B, C).
% Rule 35
mother(A, C) :- daughter(A, B), grandmother(B, C).
% Rule 36
mother(A, C) :- son(A, B), grandmother(B, C).
% Rule 37
grandson(A, C) :- grandson(A, B), brother(B, C).
% Rule 38
granddaughter(A, C) :- grandson(A, B), sister(B, C).
% Rule 39
grandson(A, C) :- son(A, B), son(B, C).
% Rule 40
grandson(A, C) :- granddaughter(A, B), brother(B, C).
% Rule 41
grandson(A, C) :- daughter(A, B), son(B, C).
% Rule 42
granddaughter(A, C) :- daughter(A, B), daughter(B, C).
% Rule 43
granddaughter(A, C) :- son(A, B), daughter(B, C).
% Rule 44
grandfather(A, C) :- brother(A, B), grandfather(B, C).
% Rule 45
grandfather(A, C) :- mother(A, B), father(B, C).
% Rule 46
grandmother(A, C) :- sister(A, B), grandmother(B, C).
% Rule 47
granddaughter(A, C) :- granddaughter(A, B), sister(B, C).
% Rule 48
grandfather(A, C) :- sister(A, B), grandfather(B, C).
% Rule 49
grandmother(A, C) :- brother(A, B), grandmother(B, C).
% Rule 50
grandmother(A, C) :- father(A, B), mother(B, C).
% Rule 51
grandfather(A, C) :- father(A, B), father(B, C).
% Rule 52
grandmother(A, C) :- mother(A, B), mother(B, C).
% Rule 53
son_in_law(A, C) :- daughter(A, B), husband(B, C).
% Rule 54
daughter_in_law(A, C) :- son(A, B), wife(B, C).
% Rule 55
grandson(A, C) :- husband(A, B), grandson(B, C).
% Rule 56
father_in_law(A, C) :- husband(A, B), father(B, C).
% Rule 57
mother_in_law(A, C) :- husband(A, B), mother(B, C).
% Rule 58
granddaughter(A, C) :- wife(A, B), granddaughter(B, C).
% Rule 59
granddaughter(A, C) :- husband(A, B), granddaughter(B, C).
% Rule 60
father_in_law(A, C) :- wife(A, B), father(B, C).
% Rule 61
grandson(A, C) :- wife(A, B), grandson(B, C).
% Rule 62
mother_in_law(A, C) :- wife(A, B), mother(B, C).
'''

print(rules)