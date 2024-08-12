gen_rule_prompt = """Story: [Verdie] waved good bye to her dad [Henry] for the day and went next door with her sister [Amanda]. [Henry]'s daughter, [Amanda], went to the city this weekend. She spent her time there visiting her grandfather, [Kyle], and had a wonderful time with him.
Query: (“Verdie”, “Kyle”)
Semantic Parse: father("Verdie", "Henry"). sister("Verdie", "Amanda"). daughter("Henry", "Amanda"). grandfather("Amanda", "Kyle").
Answer: grandfather(“Verdie”, “Kyle”)
Explain: grandfather(A, C) :- sister(A, B), grandfather(B, C).

Story: [Allen]'s father, [Eric], bought him some ice cream. [Karen] was baking cookies for her grandson, [Allen]. [Allen]'s brother [Arthur] came home from school, so she baked some extra for him, too. [Eric]'s son, [Arthur], was ill and needed to be picked up at school. [Eric] hurried to his side.
Query: (“Karen”, “Arthur”)
Semantic Parse: father("Allen", "Eric"). grandson("Karen", "Allen"). brother("Allen", "Arthur"). son("Eric", "Arthur").
Answer: grandson("Karen","Arthur")
Explain: grandson(A, C) :- grandson(A, B), brother(B, C).

Story: [Karen] was spending the weekend with her grandson, [Eddie]. [Eddie]'s sister [Michelle] was supposed to come too, but she was busy and could n't make it. [Theresa] took her daughter, [Michelle], out to High Tea yesterday afternoon. [Eddie]'s mother [Theresa] baked brownies for dessert after they had dinner.
Query: (“Karen”, “Michelle”)
Semantic Parse: grandson("Karen", "Eddie"). sister("Eddie", "Michelle"). daughter("Theresa", "Michelle"). mother("Eddie", "Theresa").
Answer: granddaughter(“Karen”, “Michelle”)
Explain: granddaughter(A, C) :- grandson(A, B), sister(B, C)."""

semantic_prompt = """Story: [Verdie] waved good bye to her dad [Henry] for the day and went next door with her sister [Amanda]. [Henry]'s daughter, [Amanda], went to the city this weekend. She spent her time there visiting her grandfather, [Kyle], and had a wonderful time with him.
Semantic Parse: father("Verdie", "Henry"). daughter("Henry", "Verdie"). sister("Verdie", "Amanda"). sister("Amanda", "Verdie"). daughter("Henry", "Amanda"). father("Amanda", "Henry"). grandfather("Amanda", "Kyle"). granddaughter("Kyle", "Amanda").

Story: [Michelle] was excited for today, its her daughter's, [Theresa], spring break. She will finally get to see her. [Michael] was busy and sent his wife, [Marlene], instead. [Kristen] loved to care for her newborn child [Ronald]. [Eric]'s son is [Arthur].
Semantic Parse: daughter("Michelle", "Theresa"). mother("Theresa", "Michelle"). wife("Michael", "Marlene"). husband("Marlene", "Michael") child("Kristen", "Ronald"), mother("Kristen", "Ronald"). son("Eric", "Arthur"), father("Arthur", "Eric").

Story: [Vernon] was present in the delivery room when his daughter [Raquel] was born, but when his daughter [Constance] was born he was too sick. [Vernon] and his daughter [Margaret] went to the movies. [Constance], [Margaret]'s sister, had to stay home as she was sick.
Semantic Parse: daughter("Vernon", "Raquel"). father("Raquel", "Vernon"). daughter("Vernon", "Constance"). father("Constance", "Vernon"). daughter("Vernon", "Margaret"). father("Margaret", "Vernon"). sister("Margaret", "Constance").
"""
relations = [
    "sibling",
    "child",
    "inv-child",
    "in-law",
    "inv-in-law",
    "grand",
    "inv-grand",
    "un",
    "inv-un",
    "SO",
]