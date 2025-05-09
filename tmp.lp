
  %!trace {"son(%, %)", A, C} son(A, C).
  %!trace {"daughter(%, %)", A, C} daughter(A, C).
  %!trace {"father(%, %)", A, C} father(A, C).
  %!trace {"mother(%, %)", A, C} mother(A, C).
  %!trace {"daughter-in-law(%, %)", A, C} daughter_in_law(A, C).
  %!trace {"son-in-law(%, %)", A, C} son_in_law(A, C).
  %!trace {"grandson(%, %)", A, C} grandson(A, C).
  %!trace {"granddaughter(%, %)", A, C} granddaughter(A, C).
  %!trace {"grandfather(%, %)", A, C} grandfather(A, C).
  %!trace {"grandmother(%, %)", A, C} grandmother(A, C).
  %!trace {"aunt(%, %)", A, C} aunt(A, C).
  %!trace {"uncle(%, %)", A, C} uncle(A, C).
  %!trace {"niece(%, %)", A, C} niece(A, C).
  %!trace {"nephew(%, %)", A, C} nephew(A, C).
  %!trace {"sister(%, %)", A, C} sister(A, C).
  %!trace {"brother(%, %)", A, C} brother(A, C).
  %!trace {"mother-in-law(%, %)", A, C} mother_in_law(A, C).
  %!trace {"father-in-law(%, %)", A, C} father_in_law(A, C).
  %!trace {"husband(%, %)", A, C} husband(A, C).
  %!trace {"wife(%, %)", A, C} wife(A, C).

  %!trace_rule {"son(%, %) because son(%, %) and brother(%, %)", A, C, A, B, B, C}
  son(A, C) :- son(A, B), brother(B, C), A!=C.
  %!trace_rule {"daughter(%, %) because daughter(%, %) and sister(%, %)", A, C, A, B, B, C}
  daughter(A, C) :- daughter(A, B), sister(B, C), A!=C.
  %!trace_rule {"daughter(%, %) because son(%, %) and sister(%, %)", A, C, A, B, B, C}
  daughter(A, C) :- son(A, B), sister(B, C), A!=C.
  %!trace_rule{"son(%, %) because daughter(%, %) and brother(%, %)", A, C, A, B, B, C}
  son(A, C) :- daughter(A, B), brother(B, C), A!=C.
  %!trace_rule {"sister(%, %) because sister(%, %) and sister(%, %)", A, C, A, B, B, C}
  sister(A, C) :- sister(A, B), sister(B, C), A!=C.
  %!trace_rule {"brother(%, %) because sister(%, %) and brother(%, %)", A, C, A, B, B, C}
  brother(A, C) :- sister(A, B), brother(B, C), A!=C.
  %!trace_rule {"sister(%, %) because daughter(%, %) and aunt(%, %)", A, C, A, B, B, C}
  sister(A, C) :- daughter(A, B), aunt(B, C), A!=C.
  %!trace_rule {"brother(%, %) because daughter(%, %) and uncle(%, %)", A, C, A, B, B, C}
  brother(A, C) :- daughter(A, B), uncle(B, C), A!=C.
  %!trace_rule {"brother(%, %) because son(%, %) and uncle(%, %)", A, C, A, B, B, C}
  brother(A, C) :- son(A, B), uncle(B, C), A!=C.
  %!trace_rule {"brother(%, %) because brother(%, %) and brother(%, %)", A, C, A, B, B, C}
  brother(A, C) :- brother(A, B), brother(B, C), A!=C.
  %!trace_rule {"sister(%, %) because father(%, %) and daughter(%, %)", A, C, A, B, B, C}
  sister(A, C) :- father(A, B), daughter(B, C), A!=C.
  %!trace_rule {"brother(%, %) because mother(%, %) and son(%, %)", A, C, A, B, B, C}
  brother(A, C) :- mother(A, B), son(B, C), A!=C.
  %!trace_rule {"brother(%, %) because father(%, %) and son(%, %)", A, C, A, B, B, C}
  brother(A, C) :- father(A, B), son(B, C), A!=C.
  %!trace_rule {"sister(%, %) because mother(%, %) and daughter(%, %)", A, C, A, B, B, C}
  sister(A, C) :- mother(A, B), daughter(B, C), A!=C.
  %!trace_rule {"father(%, %) because brother(%, %) and father(%, %)", A, C, A, B, B, C}
  father(A, C) :- brother(A, B), father(B, C), A!=C.
  %!trace_rule {"sister(%, %) because brother(%, %) and sister(%, %)", A, C, A, B, B, C}
  sister(A, C) :- brother(A, B), sister(B, C), A!=C.
  %!trace_rule {"sister(%, %) because son(%, %) and aunt(%, %)", A, C, A, B, B, C}
  sister(A, C) :- son(A, B), aunt(B, C), A!=C.
  %!trace_rule {"mother(%, %) because brother(%, %) and mother(%, %)", A, C, A, B, B, C}
  mother(A, C) :- brother(A, B), mother(B, C), A!=C.
  %!trace_rule {"father(%, %) because sister(%, %) and father(%, %)", A, C, A, B, B, C}
  father(A, C) :- sister(A, B), father(B, C), A!=C.
  %!trace_rule {"mother(%, %) because sister(%, %) and mother(%, %)", A, C, A, B, B, C}
  mother(A, C) :- sister(A, B), mother(B, C), A!=C.
  %!trace_rule {"aunt(%, %) because mother(%, %) and sister(%, %)", A, C, A, B, B, C}
  aunt(A, C) :- mother(A, B), sister(B, C), A!=C.
  %!trace_rule {"uncle(%, %) because father(%, %) and brother(%, %)", A, C, A, B, B, C}
  uncle(A, C) :- father(A, B), brother(B, C), A!=C.
  %!trace_rule {"father(%, %) because daughter(%, %) and grandfather(%, %)", A, C, A, B, B, C}
  father(A, C) :- daughter(A, B), grandfather(B, C), A!=C.
  %!trace_rule {"aunt(%, %) because father(%, %) and sister(%, %)", A, C, A, B, B, C}
  aunt(A, C) :- father(A, B), sister(B, C), A!=C.
  %!trace_rule {"uncle(%, %) because mother(%, %) and brother(%, %)", A, C, A, B, B, C}
  uncle(A, C) :- mother(A, B), brother(B, C), A!=C.
  %!trace_rule {"daughter(%, %) because husband(%, %) and daughter(%, %)", A, C, A, B, B, C}
  daughter(A, C) :- husband(A, B), daughter(B, C), A!=C.
  %!trace_rule {"son(%, %) because wife(%, %) and son(%, %)", A, C, A, B, B, C}
  son(A, C) :- wife(A, B), son(B, C), A!=C.
  %!trace_rule {"son(%, %) because husband(%, %) and son(%, %)", A, C, A, B, B, C}
  son(A, C) :- husband(A, B), son(B, C), A!=C.
  %!trace_rule {"father(%, %) because son(%, %) and grandfather(%, %)", A, C, A, B, B, C}
  father(A, C) :- son(A, B), grandfather(B, C), A!=C.
  %!trace_rule {"niece(%, %) because brother(%, %) and daughter(%, %)", A, C, A, B, B, C}
  niece(A, C) :- brother(A, B), daughter(B, C), A!=C.
  %!trace_rule {"niece(%, %) because sister(%, %) and daughter(%, %)", A, C, A, B, B, C}
  niece(A, C) :- sister(A, B), daughter(B, C), A!=C.
  %!trace_rule {"nephew(%, %) because sister(%, %) and son(%, %)", A, C, A, B, B, C}
  nephew(A, C) :- sister(A, B), son(B, C), A!=C.
  %!trace_rule {"nephew(%, %) because brother(%, %) and son(%, %)", A, C, A, B, B, C}
  nephew(A, C) :- brother(A, B), son(B, C), A!=C.
  %!trace_rule {"daughter(%, %) because wife(%, %) and daughter(%, %)", A, C, A, B, B, C}
  daughter(A, C) :- wife(A, B), daughter(B, C), A!=C.
  %!trace_rule {" mother(%, %) because daughter(%, %) and grandmother(%, %)", A, C, A, B, B, C}
  mother(A, C) :- daughter(A, B), grandmother(B, C), A!=C.
  %!trace_rule {"mother(%, %) because son(%, %) and grandmother(%, %)", A, C, A, B, B, C}
  mother(A, C) :- son(A, B), grandmother(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because grandson(%, %) and brother(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- grandson(A, B), brother(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because granddaughter(%, %) and sister(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- grandson(A, B), sister(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because son(%, %) and son(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- son(A, B), son(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because granddaughter(%, %) and brother(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- granddaughter(A, B), brother(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because daughter(%, %) and son(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- daughter(A, B), son(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because daughter(%, %) and daughter(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- daughter(A, B), daughter(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because son(%, %) and daughter(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- son(A, B), daughter(B, C), A!=C.
  %!trace_rule {"grandfather(%, %) because brother(%, %) and grandfather(%, %)", A, C, A, B, B, C}
  grandfather(A, C) :- brother(A, B), grandfather(B, C), A!=C.
  %!trace_rule {"grandfather(%, %) because mother(%, %) and father(%, %)", A, C, A, B, B, C}
  grandfather(A, C) :- mother(A, B), father(B, C), A!=C.
  %!trace_rule {"grandmother(%, %) because sister(%, %) and grandmother(%, %)", A, C, A, B, B, C}
  grandmother(A, C) :- sister(A, B), grandmother(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because granddaughter(%, %) and sister(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- granddaughter(A, B), sister(B, C), A!=C.
  %!trace_rule {"grandfather(%, %) because sister(%, %) and grandfather(%, %)", A, C, A, B, B, C}
  grandfather(A, C) :- sister(A, B), grandfather(B, C), A!=C.
  %!trace_rule {"grandmother(%, %) because brother(%, %) and grandmother(%, %)", A, C, A, B, B, C}
  grandmother(A, C) :- brother(A, B), grandmother(B, C), A!=C.
  %!trace_rule {"grandmother(%, %) because father(%, %) and mother(%, %)", A, C, A, B, B, C}
  grandmother(A, C) :- father(A, B), mother(B, C), A!=C.
  %!trace_rule {"grandfather(%, %) because father(%, %) and father(%, %)", A, C, A, B, B, C}
  grandfather(A, C) :- father(A, B), father(B, C), A!=C.
  %!trace_rule {"grandmother(%, %) because mother(%, %) and mother(%, %)", A, C, A, B, B, C}
  grandmother(A, C) :- mother(A, B), mother(B, C), A!=C.
  %!trace_rule {"son-in-law(%, %) because daughter(%, %) and husband(%, %)", A, C, A, B, B, C}
  son_in_law(A, C) :- daughter(A, B), husband(B, C), A!=C.
  %!trace_rule {"daughter-in-law(%, %) beacause son(%, %) and wife(%, %)", A, C, A, B, B, C}
  daughter_in_law(A, C) :- son(A, B), wife(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because husband(%, %) and grandson(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- husband(A, B), grandson(B, C), A!=C.
  %!trace_rule {"father-in-law(%, %) because husband(%, %) and father(%, %)", A, C, A, B, B, C}
  father_in_law(A, C) :- husband(A, B), father(B, C), A!=C.
  %!trace_rule {"mother-in-law(%, %) because husband(%, %) and mother(%, %)", A, C, A, B, B, C}
  mother_in_law(A, C) :- husband(A, B), mother(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because wife(%, %) and granddaughter(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- wife(A, B), granddaughter(B, C), A!=C.
  %!trace_rule {"granddaughter(%, %) because husband(%, %) and granddaughter(%, %)", A, C, A, B, B, C}
  granddaughter(A, C) :- husband(A, B), granddaughter(B, C), A!=C.
  %!trace_rule {"father-in-law(%, %) because wife(%, %) and father(%, %)", A, C, A, B, B, C}
  father_in_law(A, C) :- wife(A, B), father(B, C), A!=C.
  %!trace_rule {"grandson(%, %) because wife(%, %) and grandson(%, %)", A, C, A, B, B, C}
  grandson(A, C) :- wife(A, B), grandson(B, C), A!=C.
  %!trace_rule {"daughter-in-law(%, %) because daughter(%, %) and grandmother(%, %)", A, C, A, B, B, C}
  mother_in_law(A, C) :- wife(A, B), mother(B, C), A!=C.

  son("Theresa", "Darnell"). mother("Darnell", "Theresa"). daughter("Theresa", "Amanda"). mother("Amanda", "Theresa"). sister("Darnell", "Michelle"). brother("Michelle", "Darnell"). daughter("Michelle", "Theresa"). mother("Theresa", "Michelle").

  %!show_trace son(A, C).
  %!show_trace daughter(A, C).
  %!show_trace father(A, C).
  %!show_trace mother(A, C).
  %!show_trace daughter_in_law(A, C).
  %!show_trace son_in_law(A, C).
  %!show_trace grandson(A, C).
  %!show_trace granddaughter(A, C).
  %!show_trace grandfather(A, C).
  %!show_trace grandmother(A, C).
  %!show_trace aunt(A, C).
  %!show_trace uncle(A, C).
  %!show_trace niece(A, C).
  %!show_trace nephew(A, C).
  %!show_trace sister(A, C).
  %!show_trace brother(A, C).
  %!show_trace mother_in_law(A, C).
  %!show_trace father_in_law(A, C).
  %!show_trace husband(A, C).
  %!show_trace wife(A, C).
  