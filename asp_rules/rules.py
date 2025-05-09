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
%sister(A, C) :- daughter(A, B), aunt(B, C).
% Rule 8
%brother(A, C) :- daughter(A, B), uncle(B, C).
% Rule 9
%brother(A, C) :- son(A, B), uncle(B, C).
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
%sister(A, C) :- son(A, B), aunt(B, C).
% Rule 18
mother(A, C) :- brother(A, B), mother(B, C).
% Rule 19
father(A, C) :- sister(A, B), father(B, C).
% Rule 20
mother(A, C) :- sister(A, B), mother(B, C).
% Rule 21
%aunt(A, C) :- mother(A, B), sister(B, C).
% Rule 22
%uncle(A, C) :- father(A, B), brother(B, C).
% Rule 23
father(A, C) :- daughter(A, B), grandfather(B, C).
% Rule 24
%aunt(A, C) :- father(A, B), sister(B, C).
% Rule 25
%uncle(A, C) :- mother(A, B), brother(B, C).
% Rule 26
daughter(A, C) :- husband(A, B), daughter(B, C).
% Rule 27
son(A, C) :- wife(A, B), son(B, C).
% Rule 28
son(A, C) :- husband(A, B), son(B, C).
% Rule 29
father(A, C) :- son(A, B), grandfather(B, C).
% Rule 30
%niece(A, C) :- brother(A, B), daughter(B, C).
% Rule 31
%niece(A, C) :- sister(A, B), daughter(B, C).
% Rule 32
%nephew(A, C) :- sister(A, B), son(B, C).
% Rule 33
%nephew(A, C) :- brother(A, B), son(B, C).
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
%son_in_law(A, C) :- daughter(A, B), husband(B, C).
% Rule 54
%daughter_in_law(A, C) :- son(A, B), wife(B, C).
% Rule 55
grandson(A, C) :- husband(A, B), grandson(B, C).
% Rule 56
%father_in_law(A, C) :- husband(A, B), father(B, C).
% Rule 57
%mother_in_law(A, C) :- husband(A, B), mother(B, C).
% Rule 58
granddaughter(A, C) :- wife(A, B), granddaughter(B, C).
% Rule 59
granddaughter(A, C) :- husband(A, B), granddaughter(B, C).
% Rule 60
%father_in_law(A, C) :- wife(A, B), father(B, C).
% Rule 61
grandson(A, C) :- wife(A, B), grandson(B, C).
% Rule 62
%mother_in_law(A, C) :- wife(A, B), mother(B, C).

%Generated from 0.51
%grandchild(A, C) :- daughter(A, B), child(B, C).


%Rule sinh thêm 0.85 lần 1 - TURN 1 0.7 - TURN 1 0.5
daughter_in_law(A, C) :- son(A, B), wife(B, C).
%TURN 2 0.5 - STR 2
%father(A, C) :- daughter(A, B), grandfather(B, C).
%Rule sinh theem 0.85 laanf 2 - TURN 2 0.7 - TURN 3 0.5
nephew(A, C) :- sister(A, B), son(B, C).
%Rule sinh them 0.85 turn 3 - TURN 3 0.7 - TURN 4 0.5
father_in_law(A, C) :- wife(A, B), father(B, C).
%TURN 4 0.7 - str 6 - TURN 6 0.5 (STR 5 looix)
%sister(A, B) :- daughter(A, C), aunt(C, B).
%turn 7 0.85 - TURN 8 0.7 - TURN 9 0.5
nephew(A, C) :- brother(A, B), son(B, C).
%TURN 10 0.5 STR 12
%mother(A, C) :- daughter(A, B), grandmother(B, C).
%turn 9 0.7 - STR 14 - TURN 11 0.5
brother(A, C) :- son(A, B), uncle(B, C).
%turn 8 0.85 - turn 10 0.7 - TURN 12 0.5
niece(A, C) :- sister(A, B), daughter(B, C).
%STR 17 k dc car 0.7 0.5

%turn 10 - TURN 12 0.7 - TURN 14 0.5 - str 20
mother_in_law(A, C) :- husband(A, B), mother(B, C).
%turn 9 - TURN 11 0.7 -  str 17 - TURN 13 - str 17
father_in_law(A, C) :- husband(A, B), father(B, C).
%turn 13 0.7 - turn 15 0.51
aunt(A, C) :- sister(B, C), mother(A, B).
%TURN 16 0.51 STR 24
%grandmother(A, C) :- father(A, B), mother(B, C).
%TURN 17 0.51 STR 25
%mother(A, C) :- son(A, B), grandmother(B, C).
%TURN 18 0.51 - STR 26
%grandfather(A, C) :- mother(A, B), father(B, C).
%TURN 14: STR 29 crack - turn 19 0.51 crack
%TURN 15 0.7 STR 30 - TURN 20 0.51
uncle(C, A) :- brother(B, A), father(C, B).
%TURN 16 - STR 31 0.7 => STORY sai, cos 2 entity - turn 21 0.51
%TURN 22 0.51 STR 34
%grandmother(C, A) :- mother(B, A), mother(C, B).
%TURN 17 0.7 - STR 35 - turn 23 0.51
uncle(A, C) :- mother(A, B), brother(B, C).
%TURN 18 str 38 - error - turn 24 0.51
%turn 19 str 40 - turn 25 0.51
aunt(A, C) :- father(A, B), sister(B, C).
%TURN 26 str41
%father(A, C) :- son(A, B), grandfather(B, C).
%turn 11 - turn 20 0.7 - STR 59 - turn 27 0.51
mother_in_law(A, C) :- wife(A, B), mother(B, C).
%turn 12 - TURN 21 0.7 - STR 67 - turn 28 0.5
niece(A, C) :- brother(A, B), daughter(B, C).
%TURN 22 0.7 - str 69 - turn 29 0.5
sister(A, C) :- son(A, B), aunt(B, C).
%turn 13 - TURN 23 0.7 - STR 72 - turn 30 0.5
son_in_law(A, B) :- daughter(A, C), husband(C, B).
%turn 24 0.7 - STR 83 - turn 30 0.5
brother(C, A) :- daughter(C, B), uncle(B, A).
%TURN 31 0.5
%grandfather(A, C) :- father(A, B), father(B, C).
%TURN 32 - STr 90
%grandmother(C, A) :- grandmother(B, A), brother(C, B).
%STR 106 sai
%STR 125
%grandfather(B, A) :- sister(B, C), grandfather(C, A).
%STR 145
%grandfather(A, C) :- brother(A, B), grandfather(B, C).
%STR 214, 218, 248 293 340
%STR 359
%grandmother(A, C) :- sister(A, B), grandmother(B, C).
%STR
'''

print(rules)