# La Pensée Python, Comment raisonner comme un scientiste de l'informatique

traduction du livre: Think Python, How To Think Like A Computer Scientist d'Allan Downey

par Abdur-Rahmaan Janhangeer de l'Ile Maurice

# Indexe

- [Chapitre 1: Le chemin de la programmation](#ch1)
- [Chapitre 2: Variables, expressions et déclarations](#ch2)
- [Chapitre 3: Les fonctions](#ch3)
- [Chapitre 4: Etude de cas: conception d'interface](#ch4)
- [Chapitre 5: Etude de cas: conditions et récursivité](#ch5)

# Chapitre 1<a name="ch1"></a>

## Le chemin de la programmation

Le but de ce livre est de vous apprendre à penser comme un informaticien. Cette façon de penser combine certaines des meilleures caractéristiques des maths, de l'ingénierie et des sciences naturelles.
Comme les mathématiciens, les informaticiens utilisent des langages formels pour désigner des idées (en particulier les calculs). Comme les ingénieurs, ils conçoivent des choses, assemblent des composants dans des systèmes et évaluent les compromis entre les alternatives. Comme les scientifiques, ils observent le comportement des systèmes complexes, forment des hypothèses et testent des prédictions.

La compétence la plus importante pour un informaticien est la résolution de problèmes. La résolution des problèmes signifie la capacité de formuler des problèmes, réfléchir de manière créative aux solutions et exprimer une solution claire et précise. Dans l'affirmative, le processus d'apprentissage au programmation est une excellente occasion d’affiner ses compétences en matière de résolution de problèmes. C'est pourquoi ce chapitre s'appelle,
"Le chemin de la programmation".

À un niveau, vous apprendrez à programmer, une compétence utile en soi. Sur un autre niveau, vous utiliserez la programmation comme un moyen d'atteindre une fin. À mesure que nous progressons, cette fin deviendra plus claire.

1.1 Qu'est-ce qu'un programme?

Un programme est une séquence d'instructions qui spécifie comment effectuer un calcul. Le calcul peut être quelque chose de mathématique, comme la résolution d'un système d'équations ou trouver les racines d'un polynôme, mais il peut également s'agir d'un calcul symbolique, comme la recherche, remplacer du texte dans un document ou quelque chose de graphique, comme le traitement d'une image ou jouer une vidéo.

Les détails sont différents dépendant des langues, mais quelques instructions de base apparaissent dans la plupart des langues:

Entrée: Obtenez des données du clavier, d'un fichier, du réseau ou d'un autre appareil.

Sortie: afficher les données sur l'écran, l'enregistrer dans un fichier, envoie sur réseau, etc.

Math: effectuez des opérations mathématiques de base comme addition et multiplication.

Exécution conditionnelle: vérifier certaines conditions et exécuter le code approprié.

Répétition: Effectuez une action répétée, habituellement avec une certaine variation.

Croyez-le ou non, c'est à peu près tout ce qu'il y a à faire. Chaque programme que vous avez déjà utilisé, quelle que soit la complexité, se compose d'instructions qui ressemblent à peu près à celles-ci. Ainsi, vous pouvez penser à la programmation en tant que processus de rupture d'une tâche complexe en de sous-tâches plus petites et plus petites jusqu'à ce que les sous-tâches soient assez simples pour être exécutées avec une de ces instructions de base.

## 1.2 Exécuter Python

L'un des défis de commencer avec Python est que vous devrez peut-être installer Python et logiciels relatifs sur votre ordinateur. Si vous connaissez votre système d’exploitation, et surtout si vous êtes à l'aise avec l'interface ligne de commande, vous n'aurez aucun problème pour installer Python. Mais pour les débutants, il peut être douloureux de connaître le système d'administration et la programmation en même temps.

Pour éviter ce problème, je vous recommande de commencer à exécuter Python dans un navigateur. Plus tard, lorsque vous êtes à l'aise avec Python, je ferai des suggestions pour installer Python sur votre ordinateur.

Il existe un certain nombre de pages Web que vous pouvez utiliser pour exécuter Python. Si vous avez déjà un favori, allez-y et utilisez-le. Sinon, je recommande PythonAnywhere. Voyez les instructions sur http://tinyurl.com/thinkpython2e

Il existe deux versions de Python, appelées Python 2 et Python 3. Elles sont très similaires, donc si vous en apprendrez un, il est facile de passer à l'autre. En fait, il n'y a que quelques différences que vous rencontrerez en tant que débutant. Ce livre est écrit pour Python 3, mais j'ai inclu des notes sur Python 2.

L'interpréteur Python est un programme qui lit et exécute le code Python. En fonction, dépendent sur votre environnement, vous pouvez lancer l'interprète en cliquant sur une icône ou en tapant python sur une ligne de commande. Quand cela commence, vous devriez voir:

```python
Python 3.4.0 (default, Jun 19 2015, 14:20:21)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Les trois premières lignes contiennent des informations sur l'interprète et le système d'exploitation actuel, donc il pourrait être différent pour vous. Mais vous devez vérifier que le numéro de version, qui est 3.4.0 dans cet exemple, commence par 3, ce qui indique que vous utilisez Python 3. Si cela commence avec 2, vous exécutez (vous l'avez deviné) Python 2.

La dernière ligne est indique que l'interprète est prêt à recevoir le code. Si vous tapez une ligne de code et appuyez sur Entrée (sur le clavier), l'interprète affiche le résultat:

```python
>>> 1 + 1
2
```

Maintenant, vous êtes prêt à commencer. À partir de là, je suppose que vous savez comment commencer l’interprète de Python et exécuter des lignes de code.

## 1.3 Le premier programme

Traditionnellement, le premier programme que vous écrivez dans une nouvelle langue s'appelle "Hello, World!" Parce que tout ce qu'il fait, c'est d'afficher les mots "Hello, World!". Dans Python, cela ressemble à ceci:

```python
>>> print('Hello, World!')
```

Il s'agit d'un exemple d'une déclaration d'impression, bien qu'il n'imprime en réalité rien sur papier. Il affiche un résultat sur l'écran. Dans ce cas, le résultat est les mots

```
Hello, World!
```

Les guillemets dans le programme marquent le début et la fin du texte à afficher ; ils n'apparaissent pas dans le résultat.

Les parenthèses indiquent que l'impression est une fonction. Nous aborderons les fonctions du chapitre 3.

Dans Python 2, l'instruction d'impression est légèrement différente; ce n'est pas une fonction, donc les parenthèses, ça ne sert à rien.

```python
>>> print 'Hello, World!'
```

Cette distinction aura plus de sens bientôt, mais c'est assez pour commencer.

## 1.4 Opérateurs arithmétiques

Après " Hello, World!", la prochaine étape est l'arithmétique. Python fournit aux opérateurs, qui sont des symboles spéciaux qui représentent des calculs comme addition et multiplication.

Les opérateurs +, -, et * effectuent l'addition, la soustraction et la multiplication, comme suit
exemples:

```python

>>> 40 + 2
42
>>> 43 - 1
42
>>> 6 * 7
42

#L'opérateur / exécute la division:
>>> 84/2
42,0
```

Vous pourriez vous demander pourquoi le résultat est 42.0 au lieu de 42. Je vais vous expliquer dans la prochaine section.

Enfin, l'opérateur ** effectue une exponentiation; c'est-à-dire qu'il soulève un nombre à une puissance:

```python
>>> 6 ** 2 + 6
42
```

Dans certaines autres langues, ^ est utilisé pour l'exponentiation, mais en Python, c'est un opérateur bit à bit appelé XOR. Si vous n'êtes pas familiarisé avec les opérateurs bit à bit, le résultat vous surprendra:
```python
>>> 6 ^ 2
4
```

Je ne couvrirai pas les opérateurs bit à bit dans ce livre, mais vous pouvez les lire sur http://wiki.python.org/moin/BitwiseOperators.

## 1.5 Valeurs et types

Une valeur est l'une des choses de base avec laquelle un programme fonctionne, comme une lettre ou un numéro. Certains des valeurs que nous avons vues jusqu'ici sont 2, 42.0, et 'Hello, World!'.

Ces valeurs appartiennent à différents types: 2 est un nombre entier, 42.0 est un float alias nombre décimal et 'Hello, World!' est une chaîne (string en anglais), soi-disant parce que les lettres qu'il contient sont enfilées ensemble.

Si vous ne savez pas quel type de valeur a, l'interprète peut vous dire:
```python
>>> type (2)
<classe 'int'>
>>> type (42.0)
<classe 'float'>
>>> type (' Hello, World!')
<classe 'str'>
```

Dans ces résultats, le mot «class» est utilisé au sens d'une catégorie; un type est une catégorie de valeurs.

Il n'est pas surprenant que les entiers appartiennent au type int, les chaînes appartiennent à str et les nombres à virgule flottante à float.

Qu'en est-il des valeurs comme '2' et '42 .0 '? Ils ressemblent à des chiffres, mais ils sont en citations comme les strings.

```python
>>> type ('2')
<classe 'str'>
>>> type ('42 .0 ')
<classe 'str'>
Ils sont des strings.
```

Lorsque vous tapez un grand nombre entier, vous pourriez être tenté d'utiliser des virgules entre les groupes de chiffres, soit 1 000 000. Ce n'est pas un entier juridiquement parlant en Python, mais c'est légal :

```python
>>> 1,000,000
(1, 0, 0)
```
Ce n'est pas ce à quoi nous nous attendions du tout! Python interprète 1 000 000 comme une séquence d'entiers séparé par des virgules. Nous en apprendrons d’avantage sur ce genre de séquence plus tard.

## 1.6 Langues formelles et naturelles

Les langues sont les langues que les gens parlent, comme l'anglais, l'espagnol et le français. Ils n'étaient pas conçus par les gens (bien que les gens essayent d'imposer un ordre sur eux); ils évoluent naturellement.

Les langues formelles sont des langages conçus par des personnes pour des applications spécifiques. Par exemple, la notation utilisée par les mathématiciens est un langage formel qui est en particulier bien apte à dénoter les relations entre les nombres et les symboles. Les chimistes utilisent une langue formelle pour représenter la structure moléculaire des atomes. Et, surtout:

Les langages de programmation sont des langages formels conçus pour
exprimer les calculs.

Les langues formelles ont tendance à avoir des règles de syntaxe strictes qui régissent la structure des déclarations. Par exemple, en mathématiques, la déclaration 3 + 3 = 6 a une syntaxe correcte, mais 3+ = 3 $ 6 ne l’est pas. En chimie H2O est une formule syntaxiquement correcte, mais 2Zz n'est pas.

Les règles de syntaxe comportent deux saveurs, relatives aux tokens et à la structure. Les tokens sont les éléments basiques de la langue, tels que les mots, les chiffres et les éléments chimiques. Un des problèmes avec 3+ = 3 $ 6 est que $ n'est pas un token juridique en mathématiques (du moins à ce que je sais). De même, 2Zz n'est pas légal car il n'y a aucun élément avec l'abréviation Zz.

Le second type de règle de syntaxe concerne la façon dont les tokens sont combinés. L'équation 3 += 3 est illégal car même si + et = sont des tokens légaux, vous ne pouvez pas avoir un après l'autre. De même, dans une formule chimique, l'indice vient après le nom de l'élément, pas avant.

C'est une phr@se anglaise bien $tructurée avec t * kens invalide. Cette phrase valable tokens a, mais structure invalide avec.

Lorsque vous lisez une phrase en anglais ou une déclaration dans une langue officielle, vous devez identifier la structure (bien que dans une langue naturelle, vous faites cela de façon inconsciente). Ce
processus s'appelle parsing (analyse).

Bien que les langages formels et naturels possèdent de nombreuses caractéristiques communs : les token, la structure, et la syntaxe - il y a des différences:

ambiguïté: les langues naturelles sont pleines d'ambiguïté, auxquelles les gens s'occupent en utilisant des indices contextuels et d'autres informations. Les langues officielles sont conçues pour être presque ou totalement sans ambiguïté, ce qui signifie que toute déclaration a exactement un sens, quel que soit le contexte.

redondance: afin de compenser l'ambiguïté et de réduire les malentendus, les langues naturelles utilisent beaucoup de redondance. En conséquence, ils sont souvent détaillés. Les langues formelles sont moins redondantes et plus concises.

littéralité: les langues naturelles sont pleines d'idiome et de métaphore. Si je dis en anglais: "The penny dropped" (litt. le penny est tombé), il n'y a probablement pas de penny et rien n’est tombé (cette idiome signifie que quelqu'un a compris quelque chose après une période de confusion). Les langues formelles signifient exactement ce qu'ils disent. Parce que nous grandissons tous en parlant des langues naturelles, il est parfois difficile de s'adapter à la forme langues. La différence entre langage formel et naturel est comme la différence entre la poésie et la prose, mais plus encore:

Poésie: les mots sont utilisés pour leurs sons aussi bien que pour leur signification, et le poème entier ensemble crée un effet ou une réponse émotionnelle. L'ambiguïté n'est pas seulement souvent mais aussi délibéré.

Prose: le sens littéral des mots est plus important, et la structure contribue davantage au sens. La prose est plus susceptible d'analyse que le poésie, mais toujours ambiguë.

Programmes: la signification d'un programme informatique est sans ambiguïté et littérale, et peut être entièrement compris par l'analyse des tokens et de la structure.


Les langues formelles sont plus denses que les langues naturelles, il faut donc plus de temps pour les lire. En outre, la structure est importante, donc il n'est pas toujours préférable de lire de haut en bas, de gauche à droite. Au lieu de cela, apprenez à analyser le programme dans votre tête, identifiant les tokens et l'interprétation de la structure. Enfin, les détails sont importants. De petites erreurs dans l'orthographe et la ponctuation, dont vous pouvez vous en sortir dans des langues naturelles, peut faire une grande différence dans une langue formelle.

## 1.7 Débogage

Les programmeurs font des erreurs. Pour des raisons capricieuses, les erreurs de programmation sont appelées bugs et le processus de suivi est appelé débogage.
La programmation, et en particulier le débogage, soulève parfois de fortes émotions. Si vous êtes en face d’un bug difficile, vous pouvez vous sentir en colère, découragé ou embarrassé.
Il existe des preuves que les gens répondent naturellement aux ordinateurs comme s'ils étaient des gens. Quand ils fonctionnent bien, on les considère comme des coéquipiers, et quand ils sont obstinés ou grossiers, nous répondons à eux de la même manière que nous répondons à des personnes grossières et obstinées (Reeves and Nass, The Media Equation: How People Treat Computers, Television, and New Media Like Real People
and Places) .

Préparer à ces réactions pourrait vous aider à les traiter. Une approche consiste à penser à l'ordinateur en tant qu'employé avec certaines forces, comme la vitesse et la précision, et en particulier les faiblesses, comme le manque d'empathie et l'incapacité de saisir l’image en gros.

Votre travail consiste à être un bon gestionnaire: trouver des moyens de tirer parti des atouts et atténuer les faiblesses. Et trouver des façons d'utiliser vos émotions pour s'engager dans le problème, sans laisser vos réactions interférer avec votre capacité à travailler efficacement.

Apprendre à déboguer peut être frustrant, mais c'est une compétence précieuse qui est utile pour de nombreuses activités au-delà de la programmation. À la fin de chaque chapitre, il y a une section, comme celle-ci, avec
mes suggestions de débogage. J'espère qu'ils vous seront utiles!

## 1.8 Glossaire

résolution de problèmes / problem-solving: le processus de formulation d'un problème, la recherche d'une solution et l'exprimer.

Langage haut niveau / high-level language: un langage de programmation comme Python conçu pour être facile pour les humains à lire et à écrire.

langage de bas niveau / low-level language: un langage de programmation conçu pour être facile pour un ordinateur de parcourir; également appelé "language machine" ou "language assembly".

portabilité: une propriété d'un programme qui peut fonctionner sur plus d'un type d'ordinateur.

interprète: un programme qui lit un autre programme et l'exécute

prompt: caractères affichés par l'interprète pour indiquer qu'il est prêt à prendre une entrée de l'utilisateur.

programme: un ensemble d'instructions qui spécifient un calcul.

## 1.9 Exercices

print statement: une instruction qui amène l'interpréteur Python à afficher une valeur sur l'écran.

opérateur: un symbole spécial qui représente un calcul simple comme : addition, multiplication ou la concaténation de chaîne de caractères .

valeur: une des unités de base de données, comme un nombre ou une chaîne, qu'un programme manipule.

type: une catégorie de valeurs. Les types que nous avons vus jusqu'ici sont des entiers (type int), les nombres flottant (type float) et les chaînes (type str).

int: un type qui représente des nombres entiers.

float : un type qui représente des nombres décimaux.

string : un type qui représente des séquences de caractères.
Langue naturelle: l'une des langues que les gens parlent et qui évolue naturellement.

langage formel: l'une des langues que les gens ont conçues à des fins spécifiques, tels que la représentation d'idées mathématiques ou de programmes informatiques; toute les langues de programmation sont des langues officielles.

token : l'un des éléments de base de la structure syntaxique d'un programme, analogue à un mot dans une langue naturelle.

syntax: les règles qui régissent la structure d'un programme.

parsing / analyse: examiner un programme et analyser la structure syntaxique.

bug / bogue: une erreur dans un programme.

débogage: processus de recherche et de correction de bogues.


Exercice 1.1.
C'est une bonne idée de lire ce livre devant un ordinateur afin que vous puissiez essayer les exemples que vous allez lire.

Chaque fois que vous expérimentez avec une nouvelle fonctionnalité, vous devriez essayer de faire des erreurs. Par exemple, dans le programme «Hello World!», qu'arrive-t-il si vous laissez une des guillemets? Et qu'est-ce qui se passerait si vous quittez les deux? Que se passe-t-il si vous écrivez une mauvaise impression? Ce genre d'expérience vous aide à vous souvenir de ce que vous lisez. Cela vous aide également lorsque vous programmez, parce que vous comprenez ce que signifient les messages d'erreur. Il est préférable de faire des fautes maintenant et que plus tard et accidentellement.

1. Dans un print staement , que se passe-t-il si vous excluez l'une des parenthèses, ou les deux?

2. Si vous essayez d'imprimer une chaîne, que se passe-t-il si vous laissez une des guillemets, ou les deux?

3. Vous pouvez utiliser un signe moins pour créer un nombre négatif comme -2. Que se passe-t-il si vous mettez un + avant un nombre? Qu'en est-il de 2 ++ 2?


4. En notation mathématique, les zéros avancés sont corrects, comme en 02. Que se passe-t-il si vous essayez cela dans Python?

5. Que se passe-t-il si vous avez deux valeurs sans opérateur entre elles?

Exercice 1.2. Démarrez l'interpréteur Python et utilisez-le comme calculatrice.

1. Combien de secondes existe-t-il en 42 minutes 42 secondes?
2. Combien y a-t-il de miles en 10 kilomètres? Astuce: il y a 1,61 kilomètre dans un mile.
3. Si vous exécutez une course de 10 kilomètres en 42 minutes 42 secondes, quel est votre rythme moyen (temps par mile en minutes et secondes)? Quelle est votre vitesse moyenne en miles par heure?

# Chapitre 2 <a name="ch2"></a>

## Variables, expressions et déclarations

## 2.1 Valeurs et types

Une valeur est l'une des choses fondamentales - comme une lettre ou un chiffre - que le programme manipule. Les valeurs que nous avons vues jusqu'ici sont 2 (le résultat quand nous
ajouté 1 + 1), et "Hello World".
Ces valeurs appartiennent à différents types: 2 est un entier, et "Hello, World!" est une chaîne de charactères, soi-disant parce qu'elle contient une "chaîne" de lettres. Vous (et l'interprète) peut identifier les chaînes car elles sont placées entre guillemets.
L'instruction print fonctionne également pour les entiers.
```python
>>> print 4
4
```
Si vous n'êtes pas sûr du type d'une valeur, l'interprète peut vous le dire.

```python
>>> type ("Bonjour, Monde!")
<type 'str'>
>>> type (17)
<type 'int'>
```
Sans surprise, les chaînes appartiennent au type str et les entiers appartiennent au type int. Moins évident, les nombres avec un point décimal appartiennent à un type appelé float, car ces nombres sont représentés dans un format appelé float.

```python
>>> type (3.2)
<type 'float'>
```
Qu'en est-il des valeurs comme "17" et "3.2"? Ils ressemblent à des chiffres, mais ils sont
entre guillemets comme des chaînes.

```python
>>> type ("17")
<type 'str'>
>>> type ("3.2")
<type 'str'>
```

Ce sont des chaînes de charactères.
Lorsque vous tapez un grand entier, vous pourriez être tenté d'utiliser des virgules entrengroupes de trois chiffres, comme en 1.000.000 Ce n'est pas un entier légal en Python,
mais c'est une expression légale:

```python
>>> print 1 000 000
```

Eh bien, ce n'est pas ce que nous attendions du tout! Python interprète 1 000 000 comme liste séparée par des virgules de trois entiers, qu'elle imprime consécutivement. C'est le premier exemple que nous avons vu d'une erreur sémantique: le code s'exécute sans produisant un message d'erreur, mais il ne fait pas la "bonne" chose.

## 2.2 Variables

L'une des caractéristiques les plus puissantes d'un langage de programmation est la capacité à manipuler des variables. Une variable est un nom qui fait référence à une valeur.
L'instruction d'affectation crée de nouvelles variables et leur donne des valeurs:

```python
>>> message = "Quoi de neuf, Doc?"
>>> n = 17
>>> pi = 3.14159
```

Cet exemple fait trois affectations. Le premier affecte la chaîne "Quoi de neuf, Doc?"dans une nouvelle variable nommée message.La seconde donne l'entier 17 à n, et le troisième donne le nombre à virgule flottante 3.14159 à pi.
Une façon courante de représenter les variables sur papier est d'écrire le nom avec un flèche pointant vers la valeur de la variable. Ce genre de figure est appelé un diagramme états-transitions car il montre dans quel état se situe chacune des variables (pensez-y à l'état d'esprit de la variable). Ce diagramme montre le résultat de l'affectation:

```
"Quoi de neuf doc?"
17
3.14159
```
L'instruction print fonctionne également avec des variables.

```python
>>> print message
"Quoi de neuf doc?"
>>> print n
17
>>> print pi
3.14159
```

Dans chaque cas, le résultat est la valeur de la variable. Les variables ont aussi des types;
encore une fois, nous pouvons demander à l'interprète ce qu'ils sont.

```python
>>> type (message)
<type 'str'>
>>> type (n)
<type 'int'>
>>> type (pi)
<type 'float'>
```

Le type d'une variable est le type de la valeur à laquelle elle se réfère.

### 2.3 Noms de variables et mots-clés

Les programmeurs choisissent généralement des noms pour leurs variables qui sont significatives - ils documentent à quoi la variable est utilisée pour.
Les noms de variables peuvent être arbitrairement longs. Ils peuvent contenir à la fois des lettres et des chiffres, mais ils doivent commencer par une lettre. Bien qu'il ne soit pas intrdit d'utiliser des lettres majuscules, par convention, nous ne le faisons pas. Si vous le faites, rappelez-vous que cette affaire est importante. Bruce
et bruce sont des variables différentes.
Le caractère de soulignement () peut apparaître dans un nom. Il est souvent utilisé dans les noms avec des mots multiples, tels que mon nom ou le prix du thé en Chine.
Si vous attribuez un nom illégal à une variable, vous obtenez une erreur de syntaxe:

```python
>>> 76trombones = "grand défilé"
SyntaxError: invalid syntax
>>> plus $ = 1000000
SyntaxError: invalid syntax
>>> class = "Informatique 101"
SyntaxError: invalid syntax
```
76trombones est illégal car il ne commence pas par une lettre. plus $ est illégal parce qu'il contient un caractère illégal, le signe du dollar. Mais quel est le problème avec class?
Il s'avère que cette class est l'un des mots-clés Python. Les mots-clés définissent les règles et la structure du langage, et ils ne peuvent pas être utilisés comme noms de variables.
Python a vingt-neuf mots-clés:
```
and def exec if not return
assert del finally import or try
break elif for in pass while
class else from is print yield
continue except global lambda raise
```

Vous pourriez vouloir garder cette liste à portée de main. Si l'interprète se plaint d'un de vos noms de variables et vous ne savez pas pourquoi, voyez si c'est sur cette liste.

### 2.4 Déclarations

Une déclaration est une instruction que l'interpréteur Python peut exécuter. Nous avons vu deux types d'déclarations: print et affectations.
Lorsque vous tapez une instruction sur la ligne de commande, Python l'exécute et affiche le résultat, s'il y en a un. Le résultat d'une instruction print est une valeur.
Les instructions d'affectation ne produisent pas de résultat.
Un script contient généralement une séquence d'instructions. S'il y en a plus d'un déclaration, les résultats apparaissent un à la fois.
Par exemple, le script
print 1
x = 2
print x
produit la valeur 2.5 Évaluation des expressions 15
1
2
Encore une fois, l'instruction d'affectation ne produit aucun affichage.

## 2.5 Évaluation des expressions

Une expression est une combinaison de valeurs, de variables et d'opérateurs. Si vous tapez une expression sur la ligne de commande, l'interprète l'évalue et affiche le résultat:
>>> 1 + 1
2
Bien que les expressions contiennent des valeurs, des variables et des opérateurs, pas toutes les expressions contient tous ces éléments. Une valeur tout seul est considérée comme expression, et est donc une variable.
>>> 17
17
>>> x
2
Etonnement, évaluer une expression n'est pas tout à fait la même chose que d'imprimer un valeur.
>>> message = "Quoi de neuf, Doc?"
>>> message
"Quoi de neuf doc?"
>>> print message
"Quoi de neuf doc?"
Lorsque l'interpréteur Python affiche la valeur d'une expression, il utilise le même format que vous utiliseriez pour entrer une valeur. Dans le cas des chaînes, cela signifie qu'il inclut les guillemets. Mais si vous utilisez print, Python affiche le contenu de la chaîne sans les guillemets.
Dans un script, une expression tout seul est une déclaration légale, mais elle ne fait rien. Le script
17
3.2
"Bonjour le monde!"
1 + 1
ne produit aucune affichage. Comment changeriez-vous le script pour afficher les valeurs de ces quatre expressions?

## 2.6 Opérateurs et opérandes

Les opérateurs sont des symboles spéciaux qui représentent des calculs comme l'addition et multiplication. Les valeurs utilisées par l'opérateur sont appelées opérandes.
Ce qui suit sont toutes les expressions Python légales dont la signification est plus ou moins claire:
20 + 32 heures-1 heure * 60 + minutes minute / 60 5 ** 2 (5 + 9) * (15-7)
Les symboles +, -, et /, et l'utilisation de parenthèses pour le regroupement signifient en Python ce qu'ils veulent dire en mathématiques. L'astérisque (*) est le symbole de
multiplication, et ** est le symbole de l'exponentiation.
Quand un nom de variable apparaît à la place d'un opérande, il est remplacé par sa valeur avant que l'opération soit effectuée.
L'addition, la soustraction, la multiplication et l'exponentiation font toutes ce que vous attendez,
mais vous pourriez être surpris par la division. L'opération suivante a un
résultat inattendu:
>>> minute = 59
>>> minute / 60
0
La valeur de minute est 59, et en arithmétique conventionnelle 59 divisé par 60 est
0,98333, pas 0. La raison de l'écart est que Python effectue une division entière.
Lorsque les deux opérandes sont des entiers, le résultat doit également être un entier, et par convention, la division entière arrondit toujours vers le bas, même dans des cas comme celui-ci où
l'entier suivant est très proche.
Une solution possible à ce problème consiste à calculer un pourcentage plutôt qu'un
fraction:
>>> minute * 100/60
98
Encore une fois le résultat est arrondi vers le bas, mais au moins maintenant la réponse est environ
correct. Une autre alternative est d'utiliser la division à virgule flottante, que nous parcourerons au Chapitre 3.

## 2.7 Ordre des opérations

Lorsque plus d'un opérateur apparaît dans une expression, l'ordre d'évaluation
dépend des règles de préséance. Python suit la même préséance
règles pour ses opérateurs mathématiques que les mathématiques font. L'acronyme PEMDAS est un moyen utile de se souvenir de l'ordre des opérations :
• Les parenthèses ont la plus haute priorité et peuvent être utilisées pour forcer un
expression à évaluer dans l'ordre que vous voulez. Depuis les expressions entre parenthèses
sont évalués en premier, 2 * (3-1) est 4, et (1 + 1) ** (5-2) est 8. Vous pouvez également utiliser des parenthèses pour rendre une expression plus facile à lire, comme dans (minute * 100) / 60, même si cela ne change pas le résultat.
• L'exponentiation a la plus haute priorité suivante, donc 2 ** 1 + 1 est 3 et non
4, et 3 * 1 ** 3 est 3 et non 27.
• La multiplication et la division ont la même précédence, ce qui est plus élevé
que l'addition et la soustraction, qui ont également la même priorité. Alors
2 * 3-1 donne 5 plutôt que 4, et 2 / 3-1 est -1, pas 1 (souvenez-vous que dans
division entière, 2/3 = 0).
• Les opérateurs ayant la même priorité sont évalués de gauche à droite. Donc dans
l'expression minute * 100/60, la multiplication arrive en premier, produisant
5900/60, ce qui donne à son tour 98. Si les opérations avaient été évaluées
de droite à gauche, le résultat aurait été 59 * 1, ce qui est 59, ce qui est faux.

## 2.8 Opérations sur les chaînes

En général, vous ne pouvez pas effectuer d'opérations mathématiques sur des chaînes, même si
les chaînes ressemblent à des nombres. Les éléments suivants sont illégaux (en supposant que ce message a pour type string):
message-1 "Bonjour" / 123 message * "Bonjour" "15" +2
Fait intéressant, l'opérateur + travaille avec des chaînes, bien qu'il ne le fasse pas exactement ce que vous pourriez attendre. Pour les chaînes, l'opérateur + représente la concaténation, ce qui signifie rejoindre les deux opérandes en les reliant bout à bout. Pour
Exemple:
fruit = "banane"
bakedGood = " pain aux noix"
print fruits + bakedGood
Le résultat de ce programme est "banane pain aux noix". L'espace avant le mot noix fait partie de la chaîne, et est nécessaire pour produire l'espace entre le chaînes concaténées.
L'opérateur * travaille également sur les chaînes; il effectue la répétition. Par exemple,
"Fun" * 3 est "FunFunFun". L'un des opérandes doit être une chaîne; l'autre doit être un nombre entier.

D'une part, cette interprétation de + et * a un sens par analogie avec l'addition et multiplication. Tout comme 4 * 3 équivaut à 4 + 4 + 4, nous nous attendons à ce que "Fun" * 3
être le même que "Fun" + "Fun" + "Fun", et il est. D'un autre côté, il y a un façon significative dans laquelle la concaténation de chaînes et la répétition sont différentes de addition et multiplication entières. Pouvez-vous penser à une propriété que l'addition
et la multiplication ont et que la concaténation et la répétition n'ont pas?

## 2.9 Composition

Jusqu'à présent, nous avons examiné les éléments d'un programme-variables, expressions,et déclarations - isolément, sans parler de la façon de les combiner.
L'une des caractéristiques les plus utiles des langages de programmation est leur capacité à prendre de petits blocs de construction et de les composer. Par exemple, nous savons comment ajouter des chiffres et nous savons comment imprimer; il se trouve que nous pouvons faire les deux à la fois :
>>> print 17 + 3
20
En réalité, l'ajout doit se produire avant l'impression, de sorte que les actions ne sont pas
se passe réellement en même temps. Le fait est que toute expression impliquant les nombres, les chaînes et les variables peuvent être utilisés dans une instruction print. Vous avez
déjà vu un exemple de ceci:
print "Nombre de minutes écoulées depuis minuit:", heure * 60 + minute
Vous pouvez également placer des expressions arbitraires sur le côté droit d'une affectation :
pourcentage = (minute * 100) / 60
Cette capacité peut ne pas sembler impressionnante maintenant, mais vous verrez d'autres exemples
où la composition permet d'exprimer des calculs complexes
et concise.
Attention: Il y a des limites sur l'endroit où vous pouvez utiliser certaines expressions. Par exemple,
le côté gauche d'une instruction d'affectation doit être un nom de variable,
pas une expression. Donc, ce qui suit est illégal: minute + 1 = heure.

## 2.10 Commentaires

À mesure que les programmes deviennent plus gros et plus compliqués, ils deviennent plus difficiles à lire.
Les langages formels sont denses, et il est souvent difficile de regarder un morceau de code
et comprendre ce qu'il fait, ou pourquoi.

Pour cette raison, c'est une bonne idée d'ajouter des notes à vos programmes pour expliquer dans
langage naturel ce que le programme fait. Ces notes sont appelées commentaires,
et ils sont marqués du symbole #:
# calcule le pourcentage de l'heure qui s'est écoulée
pourcentage = (minute * 100) / 60
Dans ce cas, le commentaire apparaît sur une ligne par lui-même. Vous pouvez également mettre des commentaires
à la fin d'une ligne:
pourcentage = (minute * 100) / 60 # attention: division entière
Tout du # à la fin de la ligne est ignoré - il n'a aucun effet sur le
programme. Le message est destiné au programmeur ou aux futurs programmeurs
qui pourrait utiliser ce code. Dans ce cas, il rappelle au lecteur le
comportement toujours surprenant de la division entière.
Ce genre de commentaire est moins nécessaire si vous utilisez l'opération de division entière,
//. Il a le même effet que l'opérateur de division1
, mais cela indique que l'effet est délibéré.
pourcentage = (minute * 100) // 60
L'opérateur de division entier est comme un commentaire qui dit: "Je sais que c'est un nombre entier
division, et je l'aime comme ça! "

## 2.11 Glossaire

value: Un nombre ou une chaîne (ou une autre chose à nommer plus tard) qui peut être stockée dans une variable ou calculé dans une expression.
type: un ensemble de valeurs. Le type d'une valeur détermine comment elle peut être utilisée dans les expressions. Jusqu'à présent, les types que vous avez vus sont des entiers (type int), nombres flottants (type float) et chaînes (type string).
floating-point: Un format pour représenter des nombres avec des parties fractionnaires.
variable: un nom qui fait référence à une valeur.
statement: Une section de code représentant une commande ou une action. Jusqu'à présent, les déclarations que vous avez vues sont des affectations et des déclarations print.
affectation: une instruction qui affecte une valeur à une variable.
1Pour maintenant. Le comportement de l'opérateur de division peut changer dans les futures versions de Python.
20 Variables, expressions et déclarations
state diagrams: Représentation graphique d'un ensemble de variables et des valeurs
auquel ils se réfèrent.
keyword : mot réservé utilisé par le compilateur pour analyser un programme;
vous ne pouvez pas utiliser des mots-clés comme if, def et while comme noms de variables.
operator: Un symbole spécial qui représente un calcul simple comme l'addition,
multiplication, ou concaténation de chaîne.
Opérande: Une des valeurs sur lesquelles un opérateur opère.
expression: une combinaison de variables, d'opérateurs et de valeurs représentant
une seule valeur de résultat.
évaluer: Pour simplifier une expression en effectuant les opérations afin de
donner une seule valeur.
division entière: Opération qui divise un entier par un autre et donne
un nombre entier. La division entière ne donne que le nombre entier de fois que
Le numérateur est divisible par le dénominateur et rejette tout ce qui reste.
règles de précédance: Ensemble de règles régissant l'ordre dans lequel les expressions impliquant plusieurs opérateurs et opérandes sont évalués.
concaténer: Pour combiner deux opérandes.
composition: La capacité de combiner des expressions simples et des déclarations dans
expressions et expressions composées afin de représenter des calculs complexes
avec concision.
commentaire : Information dans un programme destiné à d'autres programmeurs (ou quiconque lit le code source) et n'a aucun effet sur l'exécution du programme.

# Chapitre 3 <a name="ch3"></a>


## Les fonctions


## 3.1 Appels de fonction


Vous avez déjà vu un exemple d'appel de fonction:
```python
>>> type ("32")
<type 'str'>
```
Le nom de la fonction est type, et il affiche le type d'une valeur ou d'une variable.
La valeur ou variable, appelée argument de la fonction, doit
être entouré de parenthèses. Il est courant de dire qu'une fonction "prend" un
argument et "renvoie" un résultat. Le résultat est appelé la valeur de retour.
Au lieu d'imprimer la valeur de retour, nous pourrions l'assigner à une variable:
```python
>>> betty = type ("32")
>>> print betty
<type 'str'>
```
Comme un autre exemple, la fonction id prend une valeur ou une variable et retourne un
entier qui agit comme un identifiant unique pour la valeur:

```python
>>> id (3)
134882108
>>> betty = 3
>>> id (betty)
134882108
```
Chaque valeur a un identifiant, qui est un nombre unique lié à l'endroit où il est stocké
dans la mémoire de l'ordinateur. L'identifiant d'une variable est l'identifiant de la valeur à
auquel il se réfère.

## 3.2 Conversion de type

Python fournit une collection de fonctions intégrée qui convertit les valeurs d'un
int à un autre. La fonction int prend n'importe quelle valeur et la convertit en entier,
si possible, ou se plaint autrement:
```python
>>> int ("32")
32
>>> int ("Bonjour")
ValueError: invalid literal for int(): Hello
```
int peut également convertir des floats en entiers, mais rappelez-vous qu'il
tronque la partie fractionnaire:
```python
>>> int (3.99999)
3
>>> int (-2.3)
-2
```
La fonction float convertit les entiers et les chaînes en float:

```python
>>> float (32)
32,0
>>> float ("3.14159")
3.14159
Enfin, la fonction str convertit en chaîne de caractères:
>>> str (32)
'32'
>>> str (3.14149)
'3.14149'
```
Il peut sembler étrange que Python distingue la valeur entière 1 du float
1,0. Ils peuvent représenter le même nombre, mais ils appartiennent à
différents types. La raison en est qu'ils sont représentés différemment dans
l'ordinateur.

## 3.3 Coertion de type

Maintenant que nous pouvons convertir entre les types, nous avons une autre façon de faire face à
la division entière. En revenant à l'exemple du chapitre précédent, supposons que
nous voulons calculer la fraction d'une heure qui s'est écoulée. Le plus évident
expression, minute / 60, fait l'arithmétique entière, donc le résultat est toujours 0, même
à 59 minutes après l'heure.

Une solution consiste à convertir la minute en float et faire la division:
```python
>>> minute = 59
>>> float (minute) / 60
0,983333333333
```
Alternativement, nous pouvons tirer parti des règles pour la conversion automatique de type,
ce qui s'appelle la coercition de type. Pour les opérateurs mathématiques, si
l'opérande est un float, l'autre est automatiquement converti en un float:
```python
>>> minute = 59
>>> minute / 60.0
0,983333333333
```

En transformant le dénominateur en float, nous forçons Python à faire la division comme on souhaitait.

## 3.4 Fonctions mathématiques

En mathématiques, vous avez probablement vu des fonctions comme le sin et le log, et on vous
a apprit à évaluer des expressions comme sin (pi / 2) et log (1 / x). D'abord, vous
évaluez l'expression entre parenthèses (l'argument). Par exemple, pi / 2 est
approximativement 1.571, et 1 / x est 0.1 (si x arrive à être 10.0).
Ensuite, vous évaluez la fonction elle-même, soit en la recherchant dans un tableau ou en
effectuer divers calculs. Le sin de 1.571 est 1, et le log de 0.1 est
-1 (en supposant que log indique la base logarithmique 10).
Ce processus peut être appliqué à plusieurs reprises pour évaluer des expressions plus complexes
comme log (1 / sin (pi / 2)). D'abord, vous évaluez l'argument le plus profond
puis la fonction, et ainsi de suite.
Python a un module de mathématiques qui fournit la plupart des fonctions mathématiques courantes.
Un module est un fichier qui contient une collection de fonctions connectées
mis ensemble.
Avant de pouvoir utiliser les fonctions d'un module, nous devons les importer:
```python
>>> import math
```
Pour appeler l'une des fonctions, nous devons spécifier le nom du module et le
nom de la fonction, séparé par un point, également appelé période. Ce format
est appelée dot notation.

```python
>>> decibel = math.log10 (17.0)
>>> angle = 1.5
>>> height = math.sin (angle)
```
La première déclaration définit le décibel au logarithme de 17, base 10. Il y a aussi
une fonction appelée log qui prend logarithme base e.
La troisième déclaration trouve le sinus de la valeur de l'angle variable.Sin et
les autres fonctions trigonométriques (cos, tan, etc.) prennent des arguments en radian.
Pour convertir des degrés en radians, diviser par 360 et multiplier par 2 * pi. Pour
par exemple, pour trouver le sinus de 45 degrés, d'abord calculer l'angle en radians et
alors prenez le sinus:
```python
>>> degrees = 45
>>> angle = degrés * 2 * math.pi / 360.0
>>> math.sin (angle)
0,707106781187
```
La constante pi fait également partie du module mathématique. Si vous connaissez votre géométrie,
vous pouvez vérifier le résultat précédent en le comparant à la racine carrée de deux
divisé par deux:
```python
>>> math.sqrt (2) / 2.0
0,707106781187
```
## 3.5 Composition

Tout comme avec les fonctions mathématiques, les fonctions Python peuvent être composées, ce qui signifie
que vous utilisez une expression dans le cadre d'une autre. Par exemple, vous pouvez utiliser
toute expression en tant qu'argument à une fonction:
```python
>>> x = math.cos (angle + math.pi / 2)
```
Cette instruction prend la valeur de pi, la divise par 2 et ajoute le résultat à
;a valeur de l'angle. La somme est ensuite passée en argument à la fonction cos.
Vous pouvez également prendre le résultat d'une fonction et le passer en argument
un autre:
```python
>>> x = math.exp (math.log (10.0))
```
Cette instruction trouve la base de log e de 10, puis augmente e à cette puissance. le
le résultat est assigné à x.

## 3.6 Ajout de nouvelles fonctions

Jusqu'à présent, nous utilisons uniquement les fonctions fournies avec Python, mais
est également possible d'ajouter de nouvelles fonctions. Créer de nouvelles fonctions pour résoudre votre
problèmes particuliers est l'une des choses les plus utiles à propos d'un usage général
langage de programmation.
Dans le contexte de la programmation, une fonction est une suite de déclarations nommés
qui effectue une opération souhaitée. Cette opération est spécifiée dans la définition du fonction.
Les fonctions que nous avons utilisées jusqu'ici ont été définies pour nous,
et ces définitions ont été cachées. C'est une bonne chose, car cela nous permet
d'utiliser les fonctions sans se soucier des détails de leurs définitions.
La syntaxe pour une définition de fonction est:
```python
def NOM (LISTE DES PARAMETRES):
    DECLARATIONS
```
Vous pouvez choisir les noms que vous voulez pour les fonctions que vous créez, sauf que
vous ne pouvez pas utiliser un nom qui est un mot clé Python. La liste des paramètres spécifie
quelles informations, le cas échéant, vous devez fournir pour utiliser la nouvella fonction.
Il peut y avoir un certain nombre d'instructions à l'intérieur de la fonction, mais elles doivent
être en retrait de la marge de gauche. Dans les exemples de ce livre, nous utiliserons un
indentation de deux espaces.
Le premier couple de fonctions que nous allons écrire n'a pas de paramètres, de sorte que le
la syntaxe ressemble à ceci:
```python
def nouvelleLigne():
    print
```
Cette fonction s'appelle nouvelleLigne. Les parenthèses vides indiquent qu'il n'a
pas de paramètres. Il contient seulement une seule instruction, qui génère une nouvelle ligne
(C'est ce qui se passe lorsque vous utilisez une commande print sans aucun
arguments.)
La syntaxe d'appel de la nouvella fonction est la même que celle de la fonction intégrée
les fonctions:
```python
print "Premiere ligne"
nouvelleLigne()
print "Deuxieme ligne"
```
La sortie de ce programme est:
Premiere ligne.

Deuxieme ligne.
Notez l'espace supplémentaire entre les deux lignes. Et si nous voulions plus d'espace
entre les lignes? Nous pourrions appeler la même fonction à plusieurs reprises:
```python
print "Premiere ligne"
nouvelleLigne()
nouvelleLigne()
nouvelleLigne()
print "Deuxieme ligne"
```
Nous pourrions écrire une nouvella fonction appelée trois lignes qui imprime trois nouveaux
lignes:
```python
def troisLignes():
    nouvelleLigne()
    nouvelleLigne()
    nouvelleLigne()
print "Premiere ligne"
troisLignes()
print "Deuxieme ligne"
```
Cette fonction contient trois instructions, toutes indentées par deux espaces.
Puisque la déclaration suivante n'est pas indentée, Python sait qu'elle ne fait pas partie de
la fonction.
Vous devriez noter quelques choses à propos de ce programme:
1. Vous pouvez appeler la même procédure plusieurs fois. En fait, c'est assez commun
et utile de le faire.
2. Vous pouvez avoir une fonction appeler une autre fonction; dans ce cas trois lignes
appelle nouvelleLigne.
Jusqu'à présent, il n'est peut-être pas clair pourquoi il vaut la peine de créer tous ces nouveaux
fonctions. En fait, il y a beaucoup de raisons, mais cette exemple démontre
deux:
• La création d'une nouvella fonction vous donne l'opportunité de nommer un groupe de
déclarations. Les fonctions peuvent simplifier un programme en cachant un calcul complexe
derrière une seule commande et en utilisant des mots anglais à la place du
codage arcane.

## 3.7 Définitions et utilisation

• Créer une nouvella fonction peut réduire la taille d'un programme en éliminant les répétitions.
Par exemple, un court chemin pour imprimer neuf nouvelles lignes consécutives
est d'appeler troisLignes trois fois.
Comme un exercice, écrivez une fonction appelée neufLignes qui utilise
troisLignes pour imprimer neuf lignes vides. Comment voulez-vous imprimer vingt-sept
nouvelles lignes?
En rassemblant les fragments de code de la section 3.6, l'ensemble du programme semble
comme cela:
```python
def nouvelleLigne ():
    print
def troisLignes ():
    nouvelle ligne()
    nouvelle ligne()
    nouvelle ligne()
print "Premiere ligne"
troisLignes ()
print "Deuxieme ligne"
```
Ce programme contient deux définitions de fonctions: nouvelleLigne et troisLignes.
Les définitions de fonctions sont exécutées comme les autres instructions, mais l'effet est
de créer la nouvella fonction. Les instructions à l'intérieur de la fonction ne sont pas
exécutés jusqu'à ce que la fonction est appelée, et la définition de la fonction ne génère pas
de output.
Comme vous pouvez vous y attendre, vous devez créer une fonction avant de pouvoir l'exécuter.
En d'autres termes, la définition de la fonction doit être exécutée avant la première fois
qu'on l'appelle.
Comme un exercice, déplacez les trois dernières lignes de ce programme vers le haut,
donc les appels de fonction apparaissent avant les définitions. Lancer le programme
et voyez quel message d'erreur vous obtenez.
Comme un autre exercice, commencez avec la version de travail du programme
et déplacer la définition de nouvelleLigne après la définition de
trois lignes. Que se passe-t-il lorsque vous exécutez ce programme?

## 3.8 Flux d'exécution

Afin de s'assurer qu'une fonction est définie avant sa première utilisation, vous devez
connaître l'ordre dans lequel les instructions sont exécutées, ce que l'on appelle le flux
d'exécution.
L'exécution commence toujours à la première déclaration du programme. Les déclarations sont
exécutés un à la fois, dans l'ordre de haut en bas.
Les définitions de fonctions ne modifient pas le déroulement de l'exécution du programme, mais
rappelez-vous que les instructions à l'intérieur de la fonction ne sont pas exécutées avant que la fonction
soit appelé. Bien que ce ne soit pas commun, vous pouvez définir une fonction dans une autre.
Dans ce cas, la définition interne n'est pas exécutée tant que la fonction externe n'est pas appelée.
Les appels de fonction sont comme un détour dans le flux d'exécution. Au lieu d'aller à la
déclaration suivante, le flux saute à la première ligne de la fonction appelée, exécute
toutes les déclarations là-bas, puis revient pour reprendre là où il s'est arrêté.
Cela semble assez simple, jusqu'à ce que vous vous souveniez qu'une fonction peut appeler
un autre. Alors qu'au milieu d'une fonction, le programme peut devoir exécuter
les déclarations dans une autre fonction. Mais en exécutant cette nouvella fonction, le
programme pourrait devoir exécuter encore une autre fonction!
Heureusement, Python est capable de garder la trace de l'endroit où il se trouve, donc à chaque fois un
fonction complètée, le programme reprend là où il s'est arrêté dans la fonction
appelé. Quand il arrive à la fin du programme, il se termine.
Quelle est la morale de ce conte sordide? Lorsque vous lisez un programme, ne lisez pas
du haut en bas. Au lieu de cela, suivez le flux d'exécution.

## 3.9 Paramètres et arguments

Certaines des fonctions intégrées que vous avez utilisées nécessitent des arguments, les valeurs qui
contrôlent comment la fonction fait son travail. Par exemple, si vous voulez trouver le
sinus d'un nombre, vous devez indiquer quel est le nombre. Ainsi, sin prend un
valeur numérique en tant qu'argument.
Certaines fonctions prennent plus d'un argument. Par exemple, pow prend deux
arguments, la base et l'exposant. Dans la fonction, les valeurs passées qui
sont affectées à des variables appelées paramètres.
Voici un exemple de fonction définie par l'utilisateur qui a un paramètre:
```python
def printDouble(bruce):
    print bruce, bruce
```
Cette fonction prend un seul argument et l'affecte à un paramètre nommé
bruce. La valeur du paramètre (à ce stade, nous n'avons aucune idée de ce que cela va
être) est imprimé deux fois, suivi d'une nouvelle ligne. Le nom bruce a été choisi pour
suggérer que le nom que vous donnez un paramètre est à vous, mais en général, vous
voulez choisir quelque chose de plus illustratif que Bruce.
La fonction printDoubla fonctionne pour tous les types qui peuvent être imprimés:
```python
>>> printDouble ('Spam')
Spam Spam
>>> printDouble (5)
5 5
>>> printDouble (3.14159)
3.14159 3.14159
```
Dans le premier appel de fonction, l'argument est une chaîne. Dans la seconde, c'est un nombre entier.
Dans le troisième, c'est un float.
Les mêmes règles de composition qui s'appliquent aux fonctions intégrées s'appliquent également aux
fonctions définies par l'utilisateur, de sorte que nous pouvons utiliser n'importe quel type d'expression comme argument de
printDouble:
```python
>>> printDouble ('Spam' * 4)
SpamSpamSpamSpam SpamSpamSpamSpam
>>> printDouble (math.cos (math.pi))
-1,0 -1,0
```
Comme d'habitude, l'expression est évaluée avant l'exécution de la fonction, donc printDouble
imprime SpamSpamSpamSpam SpamSpamSpamSpam au lieu de 'Spam' * 4 'Spam' * 4.
Comme exercice, écrivez un appel à printDouble qui imprime 'Spam' * 4
'Spam' * 4. Astuce: les strings peuvent être enfermées en simple ou en double
guillemets, et le type de citation non utilisé pour entourer la chaîne peut être
utilisé à l'intérieur comme une partie de la chaîne.
Nous pouvons également utiliser une variable comme argument:
```python
>>> michael = 'Eric, la demi-abeille.'
>>> printDouble (michael)
Eric, la demi-abeille. Eric, la demi-abeille.
```
Remarquez quelque chose de très important ici. Le nom de la variable que nous transmettons
argument (michael) n'a rien à voir avec le nom du paramètre (bruce).
Peu importe ce que la valeur a été rappelée à la maison (dans l'appelant); ici dans
printDouble, nous appelons tout le monde bruce.

## 3.10 Les variables et les paramètres locaux

Lorsque vous créez une variable locale à l'intérieur d'une fonction, elle n'existe que dans la
fonction, et vous ne pouvez pas l'utiliser à l'extérieur. Par exemple:

```python
def chatDouble (partie1, partie2):
    chat = partie1 + partie2
    printDouble (chat)
```
Cette fonction prend deux arguments, les concatène, puis imprime le
résultat deux fois. Nous pouvons appeler la fonction avec deux chaînes:

```python
>>> chant1 = "Pie Jesu domine"
>>> chant2 = "Dona eis requiem."
>>> chatDouble (chant1, chant2)
Pie Jesu domine, Dona eis requiem. Pie Jesu domine, Dona eis requiem.
```
Lorsque chatDouble se termine, la variable chat est détruite. Si nous essayons de l'imprimer,
nous avons une erreur:
```python
>>> print chat
NameError: chat
```
Les paramètres sont également locaux. Par exemple, en dehors de la fonction printDouble, il y n'y a
pa une telle chose que bruce. Si vous essayez de l'utiliser, Python va se plaindre.

## 3.11 Diagrammes de pile / stack diagram

Pour garder une trace des variables qui peuvent être utilisées où, il est parfois utile de
dessiner un diagramme de pile. Comme les diagrammes d'état, les diagrammes de pile montrent la valeur de
chaque variable, mais ils montrent également la fonction à laquelle chaque variable appartient.
Chaque fonction est représentée par un cadre. Un cadre est une boîte avec le nom de
fonction à côté d'elle et les paramètres et les variables de la fonction à l'intérieur.
Le diagramme de pile de l'exemple précédent ressemble à ceci:



L'ordre de la pile montre le déroulement de l'exécution. printDouble a été appelé par
chatDouble, et chatDouble a été appelé par main, qui est un nom spécial pour
la fonction la plus haute. Lorsque vous créez une variable en dehors de toute fonction,
elle appartient à main.
Chaque paramètre fait référence à la même valeur que son argument correspondant. Alors,
partie1 a la même valeur que chant1, partie2 a la même valeur que chant2, et
bruce a la même valeur que le chat.
Si une erreur survient lors d'un appel de fonction, Python imprime le nom de la fonction,
et le nom de la fonction qui l'a appelée, ainsi que le nom de la fonction
appelé cela, tout le chemin du retour à la principale.
Par exemple, si nous essayons d'accéder à chat depuis printDouble, nous obtenons un
```
NameError:
Traceback (innermost last):
    File "test.py", ligne 13, in __main__
    chatDouble (chant1, chant2)
    File "test.py", ligne 5, in chatDouble
    printDouble (chat)
    File "test.py", ligne 9, in printDouble
    print chat
NameError: chat
```

Cette liste de fonctions est appelée traceback. Il vous indique dans quel fichier de programme
l'erreur s'est produite, et quelle ligne, et quelles fonctions étaient en cours d'exécution à ce moment.
Il montre également la ligne de code qui a provoqué l'erreur.
Notez la similarité entre le traceback et le diagramme de pile. Ce n'est pas un
coïncidence.

## 3.12 Fonctions avec résultats

Vous avez peut-être remarqué maintenant que certaines des fonctions que nous utilisons,
comme les fonctions mathématiques, donnent des résultats. D'autres fonctions, comme nouvelleLigne, effectuent un action
mais ne renvoie pas de valeur. Cela soulève quelques questions:

1. Que se passe-t-il si vous appelez une fonction et que vous ne faites rien avec le
résultat (c'est-à-dire que vous ne l'attribuez pas à une variable ou que vous ne l'utilisez pas dans le cadre d'une plus grande
expression)?

2. Que se passe-t-il si vous utilisez une fonction sans résultat dans le cadre d'une expression,
comme nouvelleLigne () + 7?

3. Pouvez-vous écrire des fonctions qui donnent des résultats, ou êtes-vous coincé avec simple
Fonctionne comme nouvelleLigne et printDouble?
La réponse à la dernière question est que vous pouvez écrire des fonctions qui donnent des résultats,
et nous le ferons au chapitre 5.
Comme exercice, répondez aux deux autres questions en les essayant.
Lorsque vous avez une question sur ce qui est légal ou illégal en Python, un
bon moyen de savoir est de demander à l'interprète.

## 3.13 Glossaire

- function call / appel de fonction: une instruction qui exécute une fonction. Il se compose du nom
de la fonction suivie d'une liste d'arguments entre parenthèses.

- argument: Une valeur fournie à une fonction lorsque la fonction est appelée. Ce
La valeur est affectée au paramètre correspondant dans la fonction.

- return value: Le résultat d'une fonction. Si un appel de fonction est utilisé comme une expression,
la valeur de retour est la valeur de l'expression.

- type conversion: Une instruction explicite qui prend une valeur d'un type et
calcule une valeur correspondante d'un autre type.
coercition de type: Une conversion de type qui se produit automatiquement selon
les règles de coercition de Python.

- module: un fichier qui contient une collection de fonctions et de classes associées.

- dot notation: La syntaxe pour appeler une fonction dans un autre module, en spécifiant
le nom du module suivi d'un point (periode) et du nom de la fonction.

- function: Une séquence nommée d'instructions qui effectue une opération utile.
Les fonctions peuvent ou non prendre des arguments et peuvent ou non
produire un résultat.

- définition de fonction: une instruction qui crée une nouvelle fonction, en spécifiant sa
nom, les paramètres et les instructions qu'il exécute.
flux d'exécution: ordre dans lequel les instructions sont exécutées pendant un programme
courir.

- paramètre: Un nom utilisé dans une fonction pour faire référence à la valeur passée en tant que
argument.

- variable locale: Une variable définie à l'intérieur d'une fonction. Une variable locale peut seulement
être utilisé à l'intérieur de sa fonction.

- diagramme de pile: représentation graphique d'une pile de fonctions, leurs variables,
et les valeurs auxquelles ils se réfèrent.

- frame: Une boîte dans un diagramme de pile qui représente un appel de fonction. Il contient
les variables locales et les paramètres de la fonction.

- traceback: une liste des fonctions en cours d'exécution, imprimées lors d'une exécution
erreur se produit.

# Chapitre 4<a name="ch4"></a>

## Etude de cas: conception d'interface

Ce chapitre présente une étude de cas qui illustre un processus de conception de fonctions qui travaillent ensemble.

Il présente le module tortue, qui vous permet de créer des images à l'aide de graphiques tortue.
Le module tortue est inclus dans la plupart des installations Python, mais si vous utilisez Python
en utilisant PythonAnywhere, vous ne pourrez pas exécuter les exemples de tortue (au moins vous ne pouviez pas
quand j'ai écrit ceci).
Si vous avez déjà installé Python sur votre ordinateur, vous devriez pouvoir exécuter les
exemples. Sinon, c'est le bon moment pour l'installer. J'ai posté des instructions sur http:
//tinyurl.com/thinkpython2e.
Des exemples de code de ce chapitre sont disponibles sur http://thinkpython2.com/code/
polygon.py.

## 4.1 Le module tortue

Pour vérifier si vous avez le module tortue, ouvrez l'interpréteur Python et tapez

```python
>>> import turtle
>>> bob = turtle.Turtle()
```

Lorsque vous exécutez ce code, il doit créer une nouvelle fenêtre avec une petite flèche qui représente
la tortue. Fermez la fenêtre.
Créez un fichier nommé mypolygon.py et tapez le code suivant:

```python
import turtle
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
```

Le module turtle (avec un 't' minuscule) fournit une fonction appelée Turtle (avec un 'T' majuscule) qui crée un objet Turtle, que nous assignons à une variable nommée bob. print
bob affiche quelque chose comme:

```python
<turtle.Turtle object at 0xb7bfbf4c>
```

Cela signifie que bob fait référence à un objet de type Turtle tel que défini dans la tortue de module.

mainloop indique à la fenêtre d'attendre que l'utilisateur fasse quelque chose, bien que dans ce cas
il n'y a pas grand chose à faire pour l'utilisateur, sauf fermer la fenêtre.
Une fois que vous créez une tortue, vous pouvez appeler une méthode pour la déplacer dans la fenêtre. Une méthode
est similaire à une fonction, mais utilise une syntaxe légèrement différente. Par exemple, pour déplacer la tortue
vers l'avant:

```python
bob.fd (100)
```

La méthode, fd, est associée à l'objet tortue que nous appelons bob. L'appel d'une méthode est
comme faire une demande: vous demandez à Bob d'avancer.
L'argument de fd étant une distance en pixels, la taille réelle dépend de votre affichage.
Les autres méthodes que vous pouvez appeler sur une tortue sont bk pour reculer, lt pour tourner à gauche et rt
virage à droite. L'argument pour lt et rt est un angle en degrés.
En outre, chaque tortue tient un stylo, qui est soit en bas soit en haut; si le stylo est en panne, la tortue
laisse une trace quand il bouge. Les méthodes pu et pd représentent "pen up" et "pen down".
Pour dessiner un angle droit, ajoutez ces lignes au programme (après avoir créé bob et avant d'appeler la
boucle principale):

```python
bob.fd (100)
bob.lt (90)
bob.fd (100)
```
Lorsque vous exécutez ce programme, vous devriez voir Bob se déplacer vers l’est puis vers le nord, laissant deux
segments de ligne derrière.
Modifiez maintenant le programme pour dessiner un carré. Ne continuez pas tant que vous ne l'avez pas fait fonctionner!

## 4.2 Répétition simple

Les chances sont que vous avez écrit quelque chose comme ceci:

```python
bob.fd (100)
bob.lt (90)
bob.fd (100)
bob.lt (90)
bob.fd (100)
bob.lt (90)
bob.fd (100)
```

Nous pouvons faire la même chose de manière plus concise avec une déclaration. Ajouter cet exemple à
mypolygon.py et lancez-le à nouveau:

```python
for i in range(4):
    print('Hello!')
```
Vous devriez voir quelque chose comme ceci:

```
Hello!
Hello!
Hello!
Hello!
```

C'est l'utilisation la plus simple de la déclaration for; nous verrons plus tard. Mais cela devrait être
de quoi vous permettre de réécrire votre programme de dessin en carré. Ne continuez pas jusqu'à ce que vous fassiez.
Voici une déclaration qui dessine un carré:
```python
for i in range(4):
    bob.fd(100)
    bob.lt(90)
```

La syntaxe d'une instruction for est similaire à une définition de fonction. Il a un en-tête qui se termine
avec un colon et un corps en retrait. Le corps peut contenir n'importe quel nombre d'instructions.
Un déclaration for est également appelé une boucle parce que le flux d'exécution traverse le corps
puis retourne au sommet. Dans ce cas, il court le corps quatre fois.
Cette version est en fait un peu différente du précédent code de dessin car
fait un autre tour après avoir dessiné le dernier côté de la place. Le tour supplémentaire prend plus
temps, mais cela simplifie le code si nous faisons la même chose à chaque fois dans la boucle. Ce
version la a également pour effet de laisser la tortue dans la position de départ, face à la
direction de départ.

## 4.3 Exercices

Ce qui suit est une série d'exercices utilisant TurtleWorld. Ils sont censés êtres amusants, mais ils
ont un point aussi. Pendant que vous y travaillez, réfléchissez à la question.
Les sections suivantes proposent des solutions aux exercices, ne regardez donc pas avant d'avoir terminé
(ou au moins essayé).

1. Ecrivez une fonction appelée carré qui prend un paramètre nommé t, qui est une tortue. Il
doit utiliser la tortue pour dessiner un carré.
Écrivez un appel de fonction qui passe Bob en argument à square, puis exécutez le
programme à nouveau.

2. Ajoutez un autre paramètre, nommé length, au carré. Modifier le corps si long de la
les côtés est la longueur, puis modifiez l'appel de la fonction pour fournir un second argument. Executer
le programme à nouveau. Testez votre programme avec une plage de valeurs de longueur.

3. Faites une copie du carré et changez le nom en polygone. Ajouter un autre paramètre
nommée n et modifie le corps pour dessiner un polygone régulier à n côtés. Indice: le
les angles extérieurs d'un polygone régulier à n côtés sont de 360 ​​/ n degrés.

4. Écrivez une fonction appelée cercle qui prend comme paramètres une tortue, t et rayon, et
qui trace un cercle approximatif en appelant le polygone avec une longueur appropriée et
nombre de côtés. Testez votre fonction avec une plage de valeurs de r.
Astuce: déterminez la circonférence du cercle et assurez-vous que cette longueur * n =
circonférence.

5. Faire une version plus générale du cercle appelé arc qui prend un paramètre supplémentaire
angle, qui détermine quelle fraction de cercle dessiner. l'angle est en unités de degrés,
Ainsi, lorsque l'angle = 360, l'arc doit dessiner un cercle complet.

## 4.4 Encapsulation

Le premier exercice vous demande de mettre votre code de dessin carré dans une définition de fonction et
puis appelez la fonction, en passant la tortue en paramètre. Voici une solution:
```python
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(bob)
```

Les instructions les plus internes, fd et lt, sont en retrait deux fois pour montrer qu'elles sont à l'intérieur du
for loop, qui se trouve dans la définition de la fonction. La ligne suivante, square (bob), est alignée avec
la marge de gauche, qui indique la fin de la boucle for et la définition de la fonction.
À l’intérieur de la fonction, t fait référence au même bob tortue, donc t.lt (90) a le même effet que
bob.lt (90). Dans ce cas, pourquoi ne pas appeler le paramètre bob? L'idée est que t peut être n'importe quel
tortue, pas seulement bob, vous pouvez donc créer une deuxième tortue et la passer en argument

```python
alice = turtle.Turtle()
square(alice)
```

L'encapsulation d'un morceau de code dans une fonction est appelée encapsulation. Un des avantages de
l'encapsulation consiste à attacher un nom au code, qui sert de type de documentation. Un autre avantage est que si vous réutilisez le code, il est plus concis d'appeler une fonction
deux fois que de copier et coller le corps!

## 4.5 Généralisation

L'étape suivante consiste à ajouter un paramètre de longueur à square. Voici une solution:

```python
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
square(bob, 100)
```

L'ajout d'un paramètre à une fonction s'appelle la généralisation car elle fait la fonction
plus général: dans la version précédente, le carré a toujours la même taille; dans cette version c'est
peut être n'importe quelle taille.
L'étape suivante est également une généralisation. Au lieu de dessiner des carrés, le polygone dessine des
polygones régulière avec un nombre quelconque de côtés. Voici une solution:

```python
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
polygon(bob, 7, 70)
```

## 4.6. Design d'interface

Cet exemple dessine un polygone à sept côtés avec une longueur de côté 70.
Si vous utilisez Python 2, la valeur de l'angle peut être désactivée en raison de la division entière. Une
solution simple est de calculer l’angle = 360.0 / n. Le numérateur étant un nombre à virgule flottante, le résultat est un nombre à virgule flottante.
Lorsqu'une fonction a plus que quelques arguments numériques, il est facile d'oublier ce qu'ils sont,
ou dans quel ordre ils devraient être. Dans ce cas, il est souvent utile d'inclure les noms de
les paramètres de la liste d'arguments:

```python
polygon(bob, n=7, length=70)
```
Ceux-ci sont appelés des arguments de mots-clés car ils incluent les noms de paramètres en tant que "mots-clés" (à ne pas confondre avec les mots-clés Python comme while et def).
Cette syntaxe rend le programme plus lisible. C'est aussi un rappel sur la façon dont les arguments
et paramètres fonctionnent: lorsque vous appelez une fonction, les arguments sont affectés aux paramètres.

L'étape suivante consiste à écrire le cercle, qui prend un rayon, r, en tant que paramètre. Voici un simple
solution qui utilise un polygone pour dessiner un polygone à 50 côtés:

```python
import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
length = circumference / n
polygon(t, n, length)
length = circumference / n
polygon(t, n, longueur)
```

La première ligne calcule la circonférence d'un cercle de rayon r en utilisant la formule 2πr.
Puisque nous utilisons math.pi, nous devons importer des mathématiques. Par convention, les instructions d'importation sont
généralement au début du script.

n est le nombre de segments de droite dans notre approximation d'un cercle, donc la longueur est la longueur
de chaque segment. Ainsi, le polygone dessine un polygone à 50 côtés qui se rapproche d’un cercle avec
rayon r.
Une des limites de cette solution est que n est une constante, ce qui signifie que pour de très grands cercles,
les segments de ligne sont trop longs et pour les petits cercles, nous perdons du temps à dessiner très petit
segments. Une solution consisterait à généraliser la fonction en prenant n comme paramètre.
Cela donnerait à l'utilisateur (celui qui appelle le cercle) plus de contrôle, mais l'interface serait
moins propre.
L'interface d'une fonction est un résumé de son utilisation: quels sont les paramètres? Quelle
la fonction fait-elle? Et quelle est la valeur de retour? Une interface est "propre" si elle permet au
appelant à faire ce qu'il veut sans traiter les détails inutiles.
Dans cet exemple, r appartient à l'interface car il spécifie le cercle à dessiner. n est
moins approprié car cela concerne les détails de la façon dont le cercle doit être rendu.
Plutôt que d'encombrer l'interface, il est préférable de choisir une valeur appropriée de n en fonction de la circonférence:


```python
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, n, length)
```

Maintenant, le nombre de segments est un entier proche de la circumference/3, donc la longueur de chaque
le segment est d'environ 3, ce qui est assez petit pour que les cercles semblent bons, mais gros
suffisamment pour être efficace et acceptable pour tout cercle de taille.
L'ajout de 3 à n garantit que le polygone a au moins 3 côtés.

## 4.7 Refactoring

Lorsque j'ai écrit le cercle, j'ai pu réutiliser un polygone car un polygone à plusieurs côtés est un bon
approximation d'un cercle. Mais l'arc n'est pas aussi coopératif; nous ne pouvons pas utiliser polygone ou cercle pour
dessine un arc.
Une alternative consiste à commencer par une copie du polygone et à le transformer en arc. Le résultat
pourrait ressembler à ceci:

```python
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
```
La seconde moitié de cette fonction ressemble à un polygone, mais nous ne pouvons pas réutiliser un polygone sans
changer l'interface. On pourrait généraliser le polygone pour prendre un angle comme troisième argument,
mais alors le polygone ne serait plus un nom approprié! Au lieu de cela, appelons le plus
fonction générale polyligne:

```python
    def polyline(t, n, length, angle):
        for i in range(n):
            t.fd(length)
            t.lt(angle)
```

Maintenant, nous pouvons réécrire le polygone et l'arc pour utiliser la polyligne:

```python
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
```

Enfin, nous pouvons réécrire le cercle pour utiliser l'arc:

```python
def circle(t, r):
    arc(t, r, 360)
```

Ce processus de réorganisation d'un programme pour améliorer les interfaces et faciliter la réutilisation du code est
appelé refactoring. Dans ce cas, nous avons remarqué qu'il y avait un code similaire en arc et en polygone,
donc nous avons "factorisé" en polyligne.
Si nous avions prévu à l’avance, nous aurions peut-être écrit la polyligne d’abord et évité la refactorisation,
mais souvent vous ne savez pas assez au début d'un projet pour concevoir toutes les interfaces.
Une fois que vous commencez à coder, vous comprenez mieux le problème. Parfois, le refactoring est un signe
que vous avez appris quelque chose.

## 4.8 Un plan de développement

Un plan de développement est un processus d’écriture de programmes. Le processus utilisé dans ce cas
l'étude d' "encapsulation et généralisation". Les étapes de ce processus sont les suivantes:
1. Commencez par écrire un petit programme sans définition de fonction.
2. Une fois que le programme fonctionne, identifiez-en un élément cohérent, encapsulez le
pièce dans une fonction et lui donner un nom.
3. Généraliser la fonction en ajoutant les paramètres appropriés.
4. Répétez les étapes 1 à 3 jusqu'à ce que vous ayez un ensemble de fonctions de travail. Copier et coller le travail
code pour éviter de retaper (et re-déboguer).
5. Recherchez les possibilités d’améliorer le programme en procédant à un remaniement. Par exemple, si vous
avez un code similaire à plusieurs endroits, envisagez de le prendre en compte avec une
fonction générale.
Ce processus a quelques inconvénients - nous verrons des alternatives plus tard - mais cela peut être utile si
vous ne savez pas à l'avance comment diviser le programme en fonctions. Cette approche
vous permet de concevoir au fur et à mesure.

## 4.9 docstring

Un docstring est une chaîne au début d'une fonction qui explique l'interface ("doc" est
abréviation de "documentation"). Voici un exemple:

```python
def polyline(t, n, length, angle):
"""Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
for i in range(n):
    t.fd(length)
    t.lt(angle)
```
Par convention, toutes les chaînes de caractères sont des chaînes entre guillemets, également appelées chaînes multilignes.
car les triples guillemets permettent à la chaîne de s'étendre sur plusieurs lignes.

C'est concis, mais il contient l'information essentielle dont quelqu'un aurait besoin pour utiliser cette fonction. Il explique de manière concise ce que la fonction fait (sans entrer dans les détails de la façon dont
il le fait). Il explique quel effet chaque paramètre a sur le comportement de la fonction et
quel type chaque paramètre devrait être (si ce n'est pas évident).
L'écriture de ce type de documentation est une partie importante de la conception de l'interface. Une interface bien conçue devrait être simple à expliquer; si vous avez du mal à en expliquer un
de vos fonctions, peut-être l'interface pourrait être améliorée.

## 4.10 Le débogage

Une interface est comme un contrat entre une fonction et un appelant. L'appelant accepte de fournir
certains paramètres et la fonction accepte de faire certains travaux.
Par exemple, polyligne nécessite quatre arguments: t doit être une tortue; n doit être un entier;
la longueur doit être un nombre positif; et l'angle doit être un nombre, ce qui est compris
être en degrés.
Ces exigences sont appelées conditions préalables car elles sont supposées être vraies avant
la fonction commence à s'exécuter. Inversement, les conditions à la fin de la fonction sont des conditions postconduites. Les post-conditions incluent l’effet prévu de la fonction (comme dessiner une ligne
segments) et tout effet secondaire (comme déplacer la tortue ou apporter d’autres modifications).
Les conditions préalables sont la responsabilité de l'appelant. Si l'appelant viole une condition préalable (correctement documentée!) Et que la fonction ne fonctionne pas correctement, le bogue se trouve dans l'appelant, pas
la fonction.
Si les conditions préalables sont satisfaites et que les conditions de postconditions ne le sont pas, le bogue est dans la fonction.
Si vos conditions préalables et postérieures sont claires, elles peuvent aider au débogage.

## 4.11 Glossaire

- method: Fonction associée à un objet et appelée à l'aide de la notation par points.

- loop: Partie d'un programme pouvant être exécutée à plusieurs reprises.

- encapsulation: processus de transformation d'une séquence d'instructions en une définition de fonction.
- généralisation: processus de remplacement de quelque chose d'inutile (comme un nombre)
avec quelque chose de façon générale (comme une variable ou un paramètre).

- keyword argument: argument qui inclut le nom du paramètre en tant que "mot-clé".

- interface: description de l'utilisation d'une fonction, y compris le nom et les descriptions de
les arguments et la valeur de retour.

- refactoring: Processus de modification d'un programme de travail pour améliorer les interfaces de fonction
et d'autres qualités du code.
plan de développement: Un processus pour écrire des programmes.

- docstring: Chaîne qui apparaît en haut d'une définition de fonction pour documenter l'interface de la fonction.

- condition préalable: exigence qui doit être satisfaite par l'appelant avant le démarrage d'une fonction.

- postcondition: Une exigence qui devrait être satisfaite par la fonction avant sa fin.

## 4.12 exercices

Exercice 4.1. Téléchargez le code dans ce chapitre à partir de http: // thinkpython2. com / code /
polygone. py.
1. Dessinez un diagramme de pile qui montre l’état du programme pendant l’exécution du cercle (bob,
rayon). Vous pouvez faire l'arithmétique à la main ou ajouter des instructions d'impression au code.
2. La version de l'arc de la section 4.7 n'est pas très précise car l'approximation linéaire de
cercle est toujours en dehors du vrai cercle. En conséquence, la tortue se retrouve à quelques pixels de
la bonne destination. Ma solution montre un moyen de réduire l'effet de cette erreur. Lis le
code et voir si cela a du sens pour vous. Si vous dessinez un diagramme, vous pourriez voir comment cela fonctionne.
Exercice 4.2. Écrivez un ensemble de fonctions qui peut dessiner des fleurs comme dans la figure 4.1.
Solution:
http: // thinkpython2. com / code / flower. py,
nécessite également http:
// thinkpython2. com / code / polygone. py.
Exercice 4.3. Ecrivez un ensemble de fonctions qui peut dessiner des formes comme dans la Figure 4.2.
Solution: http: // thinkpython2. com / code / tarte. py.
Exercice 4.4. Les lettres de l'alphabet peuvent être construites à partir d'un nombre modéré d'éléments de base, tels que des lignes verticales et horizontales et quelques courbes. Concevoir un alphabet qui peut être dessiné
avec un nombre minimal d'éléments de base, puis écrivez les fonctions qui dessinent les lettres.
Vous devriez écrire une fonction pour chaque lettre, avec les noms draw_a, draw_b, etc., et mettre votre
fonctions dans un fichier nommé letters.py. Vous pouvez télécharger une "machine à écrire tortue" sur http: //
thinkpython2. com / code / machine à écrire. py pour vous aider à tester votre code.

Vous pouvez obtenir une solution à partir de http: // thinkpython2. com / code / lettres. py; il faut aussi
http: // thinkpython2. com / code / polygone. py.
Exercice 4.5. Lisez à propos des spirales sur http: // fr. Wikipedia. org / wiki / Spiral; puis écrire
un programme qui dessine une spirale archimédienne (ou l'une des autres sortes). Solution: http:
// thinkpython2. com / code / spirale. py.

# Chapitre 5
## Conditions et récursivité <a name="ch5"></a>

Le sujet principal de ce chapitre est l'instruction if, qui exécute un code différent en fonction de
l'état du programme. Mais je veux d'abord présenter deux nouveaux opérateurs: la division floor et
le modulus.

## 5.1 Division et la module floor

L'opérateur de division floor, //, divise deux nombres et arrondit à un entier. Par
exemple, supposons que le temps d'exécution d'un film est de 105 minutes. Vous voudrez peut-être savoir le temps
en heures. La division conventionnelle renvoie un nombre à virgule flottante:

```python
>>> minutes = 105
>>> minutes / 60
1.75
```

Mais normalement, nous n'écrivons pas des heures avec des points décimaux. La division d'étage renvoie le nombre d'heures
en entier, en laissant tomber la fraction:

```python
>>> minutes = 105
>>> hours = minutes // 60
>>> hours
1
```

Pour obtenir le reste, vous pouvez soustraire une heure en minutes:

```python
>>> remainder = minutes - hours * 60
>>> remainder
45
```

Une alternative consiste à utiliser l'opérateur de modulus,%, qui divise deux nombres et renvoie
le reste.

```python
>>> remainder = minutes % 60
>>> remainder
45
```

L'opérateur modulus est plus utile qu'il n'y paraît. Par exemple, vous pouvez vérifier si
un nombre est divisible par un autre - si x% y est zéro, alors x est divisible par y.


Vous pouvez également extraire le chiffre ou les chiffres les plus à droite d'un nombre. Par exemple, x%10
donne le chiffre le plus à droite de x (en base 10). De même, x%100 fournit les deux derniers chiffres.
Si vous utilisez Python 2, la division fonctionne différemment. L'opérateur de division, /, effectue
la division de plancher si les deux opérandes sont des nombres entiers, et la division en virgule flottante si l'un des opérandes est
un flotteur.

## 5.2 Expressions booléennes

Une expression booléenne est une expression vraie ou fausse. Les exemples suivants
utilisent l'opérateur ==, qui compare deux opérandes et produit True s'ils sont égaux
et False sinon:

```python
>>> 5 == 5
True
>>> 5 == 6
False
```

True et False sont des valeurs spéciales appartenant au type bool; ce ne sont pas des strings:

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

L'opérateur == est l'un des opérateurs relationnels; les autres sont:

<<>rewrite here<>>

Bien que ces opérations vous soient probablement familières, les symboles Python sont différents
des symboles mathématiques. Une erreur courante consiste à utiliser un seul signe égal (=) au lieu d'un
double signe égal (==). Rappelez-vous que = est un opérateur d'affectation et == est un opérateur
relationnel. Il n'y a pas de chose comme =< ou =>.

## 5.3 Opérateurs logiques

Il existe trois opérateurs logiques: and, or, et not. La sémantique (signification) de ces
opérateurs sont similaires à leur signification en anglais. Par exemple, x>0 et x<10 est vrai
seulement si x est supérieur à 0 et inférieur à 10.

n%2 == 0 ou n%3 == 0 est vrai si l’une ou les deux conditions est vraie, c’est-à-dire si le nombre
est divisible par 2 ou 3.
Enfin, l’opérateur not nie une expression booléenne, donc pas (x>y) est vrai si x>y est
False, c'est-à-dire si x est inférieur ou égal à y.
Strictement parlant, les opérandes des opérateurs logiques doivent être des expressions booléennes, mais
Python n'est pas très strict. Tout nombre différent de zéro est interprété comme True:

## 5.4. Exécution conditionnelle

```python
>>> 42 and True
True
```

Cette flexibilité peut être utile, mais certaines subtilités peuvent être déroutantes.
Vous voudrez peut-être l'éviter (sauf si vous savez ce que vous faites).

Pour écrire des programmes utiles, nous avons presque toujours besoin de pouvoir vérifier les conditions
et modifier le comportement du programme en conséquence. Les déclarations conditionnelles nous donnent ceci
aptitude. La forme la plus simple est l'instruction if:

```python
if x > 0:
print('x is positive')
```

L'expression booléenne après if s'appelle la condition. Si c'est vrai, la déclaration en retrait
s'exécute. Sinon, rien ne se passe.

les instructions if ont la même structure que les définitions de fonctions: un en-tête suivi d'un
corps en retrait. Des déclarations comme celles-ci sont appelées des déclarations composées.
Il n'y a pas de limite au nombre de déclarations pouvant apparaître dans le corps, mais il doit y avoir
au moins un. À l’occasion, il est utile d’avoir un corps sans déclaration (généralement
placekeeper pour le code que vous n'avez pas encore écrit). Dans ce cas, vous pouvez utiliser la déclaration de passage,
qui ne fait rien.

```python
if x < 0:
pass
```

TODO: besoin de gérer des valeurs négatives!

## 5.5 Exécution alternative

Une deuxième forme de l'instruction if est "exécution alternative", dans laquelle il existe deux possibilités et la condition détermine celle qui s'exécute. La syntaxe ressemble à ceci:

```python
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
```

Si le restant lorsque x est divisé par 2 est 0, alors nous savons que x est pair, et le programme
affiche un message approprié. Si la condition est fausse, la deuxième série de déclarations
s'exécute. Comme la condition doit être vraie ou fausse, l'une des alternatives s'exécutera exactement.
Les alternatives sont appelées branches, car elles sont des branches dans le flux d'exécution.

## 5.6 Chaînes conditionnels

Parfois, il y a plus de deux possibilités et nous avons besoin de plus de deux branches.
Une façon d'exprimer un calcul comme celui-là est un chaîne conditionnel:

```python
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')
```

elif est une abréviation de "else if". Encore une fois, exactement une branche sera exécutée. Il n'y a pas de limite sur
le nombre de déclarations elif. S'il y a une clause else, elle doit être à la fin, mais
cela est facultatif.

```python
if choice == 'a':
    draw_a()
elif choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()
```

Chaque condition est vérifiée dans l'ordre. Si le premier est faux, le suivant est coché, et ainsi de suite. Si un
d'entre eux est vrai, la branche correspondante s'exécute et l'instruction se termine. Même si plus de
une condition est vraie, seule la première branche vraie s'exécute.

## 5.7 Conditionals imbriqués

Un conditionnel peut aussi être imbriqué dans un autre. Nous aurions pu écrire l'exemple dans
la section précédente comme ceci:

```python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```

Le conditionnel externe contient deux branches. La première branche contient une simple déclaration.
La seconde branche contient une autre instruction if, qui comporte deux branches.
Ces deux branches sont toutes deux des déclarations simples, bien qu’elles aient pu être 
conditionnelles.
Bien que l'indentation des déclarations rendent la structure apparente, les conditionnels imbriqués deviennent difficiles à lire très rapidement. C'est une bonne idée de les éviter quand vous
pouvez.
Les opérateurs logiques permettent souvent de simplifier les instructions conditionnelles imbriquées. Par exemple, nous pouvons réécrire le code suivant en utilisant un seul conditionnel:

```python
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')
```

L'instruction print ne s'exécute que si nous passons les deux conditions, afin que nous puissions obtenir la même chose
effet avec l'opérateur et:
```python
if 0 < x and x < 10:
print('x is a positive single-digit number.')
```

Pour ce type de condition, Python fournit une option plus concise:

```python
if 0 < x < 10:
print('x is a positive single-digit number.')
```

## 5.8 Récursivité

Il est légal qu'une fonction appelle une autre; il est également légal qu'une fonction s'appelle elle-même. Cela pourrait
ne pas être évident pourquoi c'est une bonne chose, mais il s'avère être l'un des choses les
plus magiques qu'un programme puisse faire. Par exemple, regardez la fonction suivante:

```python
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
```

Si n est 0 ou négatif, il affiche le mot "Blastoff!" Sinon, il affiche n puis appelle
une fonction nommée countdown (soi-même) en passant n-1 en argument.
Que se passe-t-il si nous appelons cette fonction comme ceci?

```python
>>> countdown(3)
```

L’exécution du compte à rebours commence par n = 3, et comme n est supérieur à 0, il sort le
valeur 3, puis appelle lui-même ...
L’exécution du compte à rebours commence par n = 2, et comme n est supérieur à 0, il
génère la valeur 2 et appelle ensuite lui-même ...
L'exécution du compte à rebours commence par n = 1, et comme n est supérieur
à 0, il affiche la valeur 1, puis s'appelle lui-même ...
L'exécution du compte à rebours commence par n = 0, et comme n est
pas supérieur à 0, il affiche le mot "Blastoff!" et retorne
ensuite.

```
The countdown that got n=1 returns.
The countdown that got n=2 returns.
The countdown that got n=3 returns.
```

Et puis vous êtes de retour dans __main__. Ainsi, la sortie totale ressemble à ceci:

```python
3
2
1
Blastoff!
```

Une fonction qui s'appelle elle-même est récursive; le processus d'exécution est appelé récursivité.
Comme autre exemple, nous pouvons écrire une fonction qui imprime une chaîne n fois.

```python
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
```

Figure 5.1: Diagramme de pile

Si n <= 0, l'instruction de retour quitte la fonction. Le flux d'exécution retourne immédiatement à l'appelant et les lignes restantes de la fonction ne s'exécutent pas.
Le reste de la fonction est similaire au compte à rebours: il affiche s puis appelle lui-même pour afficher
s n - 1 fois supplémentaires. Donc, le nombre de lignes de sortie est 1 + (n - 1), ce qui totalise
à n.
Pour des exemples simples comme celui-ci, il est probablement plus facile d'utiliser une boucle for. Mais on verra des
exemples plus tard qui sont difficiles à écrire avec une boucle for et facile à écrire avec la récursivité, de sorte qu'il
est bon de commencer tôt.

## 5.9 Diagrammes de pile pour les fonctions récursives

Dans la section 3.9, nous avons utilisé un diagramme de pile pour représenter l'état d'un programme au cours d'une fonction
appel. Le même type de diagramme peut aider à interpréter une fonction récursive.
Chaque fois qu’une fonction est appelée, Python crée un cadre pour contenir les variables et paramètres.
locaux de la fonction. Pour une fonction récursive, il peut y avoir plus d'une image sur
la pile en même temps.
La figure 5.1 montre un diagramme de pile pour le compte à rebours appelé avec n = 3.
Comme d'habitude, le haut de la pile est dans le cadre de __main__. C'est vide parce que nous n'avons pas
créer des variables dans __main__ ou lui transmettre des arguments.
Les quatres images du compte à rebours ont des valeurs différentes pour le paramètre n. Le fond de la
pile, où n = 0, est appelé le cas de base. Il ne fait pas un appel récursif, donc il n'y a pas
plus de cadres.
Comme exercice, dessinez un diagramme de pile pour print_n appelé avec s = 'Hello' et n = 2. alors
écrivez une fonction appelée do_n qui prend un objet fonction et un nombre, n, comme arguments, et
qui appelle la fonction donnée n fois.

## 5.10 Récursion infinie

Si une récursivité n'atteint jamais un cas de base, elle continue à faire des appels récursifs pour toujours et le
programme ne se termine jamais. Ceci est connu comme la récursion infinie, et ce n'est généralement pas une
bonne idée. Voici un programme minimal avec une récursion infinie:

## 5.11. La saisie au clavier

```python
def recurse ():
    recurse ()
```

Dans la plupart des environnements de programmation, un programme avec une récursion infinie ne fonctionne pas vraiment
pour toujours. Python signale un message d'erreur lorsque la profondeur de récursivité maximale est atteinte:

```
maximum recursion depth is reached:
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
.
.
.
File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded
```

Cette traceback est un peu plus grande que celle que nous avons vue dans le chapitre précédent. Quand l'erreur
se produit, il y a 1000 cadres de recurse sur la pile!
Si vous rencontrez une récursion infinie par accident, révisez votre fonction pour confirmer que
il y a un cas de base qui ne fait pas un appel récursif. Et s'il y a un cas de base, vérifiez
si vous êtes assuré d'y accéder.

Les programmes que nous avons écrits jusqu'à présent n'acceptent aucune contribution de l'utilisateur. Ils font juste la même chose
chose à chaque fois.
Python fournit une fonction intégrée appelée entrée qui arrête le programme et attend la
utilisateur de taper quelque chose. Lorsque l'utilisateur appuie sur Entrée ou Retour, le programme reprend et
input renvoie ce que l'utilisateur a tapé en tant que chaîne. Dans Python 2, la même fonction est appelée input.

code here

Avant d’obtenir les commentaires de l’utilisateur, il est conseillé d’imprimer une invite indiquant à l’utilisateur
taper input peut prendre une invite en argument:

```python
>>> name = input('What...is your name?\n')
What...is your name?
Arthur, King of the Britons!
>>> name
'Arthur, King of the Britons!'
```

La séquence \ n à la fin de l'invite représente une nouvelle ligne, qui est un caractère spécial
cela provoque un saut de ligne. C'est pourquoi l'entrée de l'utilisateur apparaît sous l'invite.
Si vous vous attendez à ce que l'utilisateur tape un entier, vous pouvez essayer de convertir la valeur de retour en int:

```python
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
Qu'est-ce que la vitesse de vitesse d'une hirondelle à vide?
42
>>> int(speed)
42
```


Mais si l'utilisateur tape autre chose qu'une chaîne de chiffres, vous obtenez une erreur:
```
>>> speed = input(prompt)
Qu'est-ce que la vitesse de vitesse d'une hirondelle à vide?
Qu'est-ce que vous voulez dire, une hirondelle africaine ou européenne?
>>> int(speed)
ValueError: invalid literal for int() with base 10
```

Nous verrons comment gérer ce type d'erreur plus tard.

## 5.12 Le débogage

Lorsqu'une erreur de syntaxe ou d'exécution se produit, le message d'erreur contient beaucoup d'informations, mais
cela peut être accablant. Les parties les plus utiles sont généralement les suivantes:
- Quel type d'erreur était-ce et
- où il s'est produit.
Les erreurs de syntaxe sont généralement faciles à trouver, mais il y a quelques pièges. Les erreurs d'espacement peuvent
être difficile parce que les espaces et les onglets sont invisibles et nous sommes habitués à les ignorer.
```python
>>> x = 5
>>> y = 6
File "<stdin>", line 1
y = 6
^
IndentationError: unexpected indent
```

Dans cet exemple, le problème est que la deuxième ligne est en retrait d'un espace. Mais l'erreur
le message indique y, ce qui est trompeur. En général, les messages d’erreur indiquent où
problème a été découvert, mais l'erreur réelle peut être antérieure dans le code, parfois sur un
ligne précédente
La même chose est vraie pour les erreurs d'exécution. Supposons que vous essayiez de calculer un rapport signal / bruit
ratio en décibels. La formule est SNRdb = 10 log10 ( Psignal /Pnoise ). En python, vous pourriez
écris quelque chose comme ceci:

```python
import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
```

Lorsque vous exécutez ce programme, vous obtenez une exception:

```python
Traceback (most recent call last):
File "snr.py", line 5, in ?
decibels = 10 * math.log10(ratio)
ValueError: math domain error
```

Le message d'erreur indique la ligne 5, mais il n'y a rien de mal avec cette ligne. Pour trouver le
erreur réelle, il pourrait être utile d’imprimer la valeur du ratio, qui se révèle être 0. Le
problème est à la ligne 4, qui utilise la division au sol au lieu de la division en virgule flottante.
Vous devriez prendre le temps de lire attentivement les messages d'erreur, mais ne présumez pas que tout
ils disent est correct.

5.13. Glossaire

- Division de plancher / floor division: Un opérateur, noté //, qui divise deux nombres et arrondit à un entier inférieur (vers l'infini négatif).
- opérateur de module / modulus operator: un opérateur, noté avec un signe de pourcentage (%), qui fonctionne sur des nombres entiers
et renvoie le reste lorsqu'un nombre est divisé par un autre.

- expression booléenne: expression dont la valeur est True ou False.

- opérateur relationnel: Un des opérateurs qui compare ses opérandes: ==,! =,>, <,> = et
<=.

- opérateur logique: un des opérateurs combinant des expressions booléennes: et, ou
ne pas.

- instruction conditionnelle: une instruction qui contrôle le flux d'exécution en fonction de certains
conditions.

- condition: expression booléenne dans une instruction conditionnelle qui détermine une
branche court.

- déclaration composée: déclaration composée d'un en-tête et d'un corps. L'en-tête se termine

- avec deux points (:). Le corps est en retrait par rapport à l'en-tête.

- branch: une des séquences alternatives d'instructions dans une instruction conditionnelle.

- chained conditionnel: une instruction conditionnelle avec une série de branches alternatives.

- conditionnel imbriqué: instruction conditionnelle qui apparaît dans l'une des branches d'une autre
déclaration conditionnelle.

- instruction de retour: instruction qui entraîne la fin immédiate d'une fonction et le retour à la
votre interlocuteur.

- récursivité: processus d'appel de la fonction en cours d'exécution.

- cas de base: branche conditionnelle dans une fonction récursive qui ne fait pas un appel récursif.

- récursion infinie: récursivité qui n'a pas de cas de base ou ne l'atteint jamais. Finalement, une récursion infinie provoque une erreur d'exécution.

## 5.14 Exercices

Exercice 5.1. Le time fournit une fonction, également nommée time, qui renvoie le Greenwich Mean Time en tant "the epoch", qui est un temps arbitraire utilisé comme point de référence. Sur
Systèmes UNIX, epoch est le 1er janvier 1970.

>>> import time
>>> time.time()
1437746094.5735958
Écrivez un script qui lit l'heure actuelle et le convertit en heure, en minutes et en minutes.
secondes, plus le nombre de jours écoulés depuis l'époque.

Exercice 5.2. Le dernier théorème de Fermat dit qu'il n'y a pas d'entiers positifs a, b et c tels que
an + bn = cn
pour toute valeur de n supérieure à 2.
1. Écrivez une fonction nommée check_fermat qui prend quatre paramètres-a, b, c et n-et
vérifie si le théorème de Fermat est valide. Si n est supérieur à 2 et
an + bn = cn
le programme devrait imprimer, "Holy smokes, Fermat was wrong!" Sinon, le programme devrait
imprimer, "No, that doesn’t work."
2. Écrivez une fonction qui invite l’utilisateur à saisir des valeurs pour a, b, c et n, les convertir en
entiers, et utilise check_fermat pour vérifier s'ils violent le théorème de Fermat.
Exercice 5.3. Si on vous donne trois bâtons, vous pouvez ou non être en mesure de les organiser en triangle.
Par exemple, si l'un des bâtons fait 12 pouces de long et que les deux autres ont un pouce de long, vous ne pourrez pas
être en mesure de faire en sorte que les bâtons courts se rencontrent au milieu. Pour trois longueurs, il existe un test simple pour
voir s'il est possible de former un triangle:
Si l'une des trois longueurs est supérieure à la somme des deux autres, vous ne pouvez pas
former un triangle. Sinon, vous pouvez. (Si la somme de deux longueurs est égale à la troisième, elles
forme ce qu'on appelle un triangle "dégénéré".)
1. Écrivez une fonction nommée is_triangle qui prend trois nombres entiers comme arguments et qui imprime
soit "Yes" ou "No", selon que vous pouvez ou ne pouvez pas former un triangle à partir de bâtons
avec les longueurs données.
2. Écrivez une fonction qui invite l’utilisateur à saisir trois longueurs de bâtons, à les convertir en nombres entiers,
et utilise is_triangle pour vérifier si les bâtons de longueur donnée peuvent former un triangle.
Exercice 5.4. Quelle est la sortie du programme suivant? Dessine un diagramme de pile qui montre le
état du programme lorsqu'il imprime le résultat.

```python
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)
```
1. Que se passerait-il si vous appeliez cette fonction comme ceci: recurse (-1, 0)?
2. Ecrivez un docstring qui explique tout ce que quelqu'un devrait savoir pour pouvoir l'utiliser
fonction (et rien d'autre).
Les exercices suivants utilisent le module tortue, décrit au chapitre 4:
Exercice 5.5. Lisez la fonction suivante et voyez si vous pouvez comprendre ce qu’elle fait (voir les exemples du chapitre 4). Puis lancez-le et voyez si vous avez bien compris.

Figure 5.2: Une courbe de Koch/ Koch curve.

```python
def draw(t, length, n):
if n == 0:
return
angle = 50
t.fd(length*n)
t.lt(angle)
draw(t, length, n-1)
t.rt(2*angle)
draw(t, length, n-1)
t.lt(angle)
t.bk(length*n)
```

Exercice 5.6. La courbe de Koch est une fractale qui ressemble à la figure 5.2. Dessiner un Koch
courbe avec longueur x, tout ce que vous avez à faire est de
1. Tracez une courbe de Koch avec une longueur x / 3.
2. Tourner à gauche de 60 degrés.
3. Tracez une courbe de Koch avec une longueur x / 3.
4. Tournez à droite de 120 degrés.
5. Tracez une courbe de Koch avec une longueur x / 3.
6. Tournez à gauche de 60 degrés.
7. Tracez une courbe de Koch avec une longueur x / 3.
L'exception est si x est inférieur à 3: dans ce cas, vous pouvez simplement tracer une ligne de longueur x.
1. Écrivez une fonction appelée koch qui prend une tortue et une longueur comme paramètres, et qui utilise la
tortue pour dessiner une courbe de Koch avec la longueur donnée.
2. Écrivez une fonction appelée flocon de neige qui dessine trois courbes de Koch pour dessiner le contour d'un
flocon de neige.
Solution: http: // thinkpython2. com / code / koch. py.
3. La courbe de Koch peut être généralisée de plusieurs manières. Voir http: // en. wikipedia. org/
wiki/ Koch_ snowflake pour des exemples et implémentez votre favori.