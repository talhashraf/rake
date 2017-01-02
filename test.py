"""Testing module"""
from rake import Rake


# Dummy text.
input_string = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types."
input_string = """Hitler was born in Austria, then part of Austria-Hungary, and raised near Linz. He moved to Germany in 1913 and was decorated during his service in the German Army in World War I. He joined the German Workers' Party (DAP), the precursor of the NSDAP, in 1919 and became leader of the NSDAP in 1921. In 1923 he attempted a coup in Munich to seize power. The failed coup resulted in Hitler's imprisonment, during which time he dictated the first volume of his autobiography and political manifesto Mein Kampf ("My Struggle"). After his release in 1924, Hitler gained popular support by attacking the Treaty of Versailles and promoting Pan-Germanism, anti-Semitism, and anti-communism with charismatic oratory and Nazi propaganda. Hitler frequently denounced international capitalism and communism as being part of a Jewish conspiracy."""
# Initiate Rake class.
RAKE = Rake(input_string)
# Get phrase scores.
SCORES = RAKE.phrase_scores().iteritems()
# Sort phrases by score.
SCORES = sorted(SCORES, key=lambda (key, val): (val, key), reverse=True)
# Print phrase with its respective score.
for phrase, score in SCORES:
    print str(score).zfill(3), phrase
