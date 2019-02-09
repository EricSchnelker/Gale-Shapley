# Gale-Shapley Pseudocode
Schnelker, Sommers, Binmansour
INITIALIZE S to empty matching.
WHILE (the q containing men is not empty [therefore, the man is unmatched and hasn't proposed to every woman])
  POP m from the queue
  FOR (w, a woman's name, in the preference list of the current man)
      IF (w is unmatched)
        ADD pair m–w to matching S.
      ELSE IF (w prefers m to her current partner m')
        REMOVE pair m'–w from matching S.
        ADD pair m–w to matching S.
        ADD m' back to the queue
      ELSE
        w rejects m.
RETURN stable matching S.
