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
wiki/ Koch_ snowflake pour des exemples et implémentez votre favori.from os import listdir
from os.path import isfile, join

mypath = '../translated'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    with open(f, 'r') as trf:
        with open('newf.md', 'a') as mdf:
            mdf.write(trf.read())﻿Chapitre 1
Le chemin de la programmation

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

<page 2> 

Chapitre 1. Le chemin de la programmation

Répétition: Effectuez une action répétée, habituellement avec une certaine variation.

Croyez-le ou non, c'est à peu près tout ce qu'il y a à faire. Chaque programme que vous avez déjà utilisé, quelle que soit la complexité, se compose d'instructions qui ressemblent à peu près à celles-ci. Ainsi, vous pouvez penser à la programmation en tant que processus de rupture d'une tâche complexe en de sous-tâches plus petites et plus petites jusqu'à ce que les sous-tâches soient assez simples pour être exécutées avec une de ces instructions de base.

1.2 Exécuter Python

L'un des défis de commencer avec Python est que vous devrez peut-être installer Python et logiciels relatifs sur votre ordinateur. Si vous connaissez votre système d’exploitation, et surtout si vous êtes à l'aise avec l'interface ligne de commande, vous n'aurez aucun problème pour installer Python. Mais pour les débutants, il peut être douloureux de connaître le système d'administration et la programmation en même temps.

Pour éviter ce problème, je vous recommande de commencer à exécuter Python dans un navigateur. Plus tard, lorsque vous êtes à l'aise avec Python, je ferai des suggestions pour installer Python sur votre ordinateur.

Il existe un certain nombre de pages Web que vous pouvez utiliser pour exécuter Python. Si vous avez déjà un favori, allez-y et utilisez-le. Sinon, je recommande PythonAnywhere. Voyez les instructions sur http://tinyurl.com/thinkpython2e 

Il existe deux versions de Python, appelées Python 2 et Python 3. Elles sont très similaires, donc si vous en apprendrez un, il est facile de passer à l'autre. En fait, il n'y a que quelques différences que vous rencontrerez en tant que débutant. Ce livre est écrit pour Python 3, mais j'ai inclu des notes sur Python 2.

L'interpréteur Python est un programme qui lit et exécute le code Python. En fonction, dépendent sur votre environnement, vous pouvez lancer l'interprète en cliquant sur une icône ou en tapant python sur une ligne de commande. Quand cela commence, vous devriez voir:

Python 3.4.0 (default, Jun 19 2015, 14:20:21)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

Les trois premières lignes contiennent des informations sur l'interprète et le système d'exploitation actuel, donc il pourrait être différent pour vous. Mais vous devez vérifier que le numéro de version, qui est 3.4.0 dans cet exemple, commence par 3, ce qui indique que vous utilisez Python 3. Si cela commence avec 2, vous exécutez (vous l'avez deviné) Python 2.

La dernière ligne est indique que l'interprète est prêt à recevoir le code. Si vous tapez une ligne de code et appuyez sur Entrée (sur le clavier), l'interprète affiche le résultat:

>>> 1 + 1
2

Maintenant, vous êtes prêt à commencer. À partir de là, je suppose que vous savez comment commencer l’interprète de Python et exécuter des lignes de code.

<page 3>

1.3 Le premier programme

Traditionnellement, le premier programme que vous écrivez dans une nouvelle langue s'appelle "Hello, World!" Parce que tout ce qu'il fait, c'est d'afficher les mots "Hello, World!". Dans Python, cela ressemble à ceci:

>>> print('Hello, World!')

Il s'agit d'un exemple d'une déclaration d'impression, bien qu'il n'imprime en réalité rien sur papier. Il affiche un résultat sur l'écran. Dans ce cas, le résultat est les mots

Hello, World!

Les guillemets dans le programme marquent le début et la fin du texte à afficher ; ils n'apparaissent pas dans le résultat.

Les parenthèses indiquent que l'impression est une fonction. Nous aborderons les fonctions du chapitre 3.

Dans Python 2, l'instruction d'impression est légèrement différente; ce n'est pas une fonction, donc les parenthèses, ça ne sert à rien.

>>> print 'Hello, World!'

Cette distinction aura plus de sens bientôt, mais c'est assez pour commencer.

1.4 Opérateurs arithmétiques

Après " Hello, World!", la prochaine étape est l'arithmétique. Python fournit aux opérateurs, qui sont des symboles spéciaux qui représentent des calculs comme addition et multiplication.

Les opérateurs +, -, et * effectuent l'addition, la soustraction et la multiplication, comme suit
exemples:

>>> 40 + 2
42
>>> 43 - 1
42
>>> 6 * 7
42
L'opérateur / exécute la division:
>>> 84/2
42,0

Vous pourriez vous demander pourquoi le résultat est 42.0 au lieu de 42. Je vais vous expliquer dans la prochaine section.

Enfin, l'opérateur ** effectue une exponentiation; c'est-à-dire qu'il soulève un nombre à une puissance:

>>> 6 ** 2 + 6
42

Dans certaines autres langues, ^ est utilisé pour l'exponentiation, mais en Python, c'est un opérateur bit à bit appelé XOR. Si vous n'êtes pas familiarisé avec les opérateurs bit à bit, le résultat vous surprendra:
>>> 6 ^ 2
4
Je ne couvrirai pas les opérateurs bit à bit dans ce livre, mais vous pouvez les lire sur http://wiki.python.org/moin/BitwiseOperators.

<page 4>
 Chapitre 1. Le chemin de la programmation

1.5 Valeurs et types

Une valeur est l'une des choses de base avec laquelle un programme fonctionne, comme une lettre ou un numéro. Certains des valeurs que nous avons vues jusqu'ici sont 2, 42.0, et 'Hello, World!'.

Ces valeurs appartiennent à différents types: 2 est un nombre entier, 42.0 est un float alias nombre décimal et 'Hello, World!' est une chaîne (string en anglais), soi-disant parce que les lettres qu'il contient sont enfilées ensemble.

Si vous ne savez pas quel type de valeur a, l'interprète peut vous dire:
>>> type (2)
<classe 'int'>
>>> type (42.0)
<classe 'float'>
>>> type (' Hello, World!')
<classe 'str'>

Dans ces résultats, le mot «class» est utilisé au sens d'une catégorie; un type est une catégorie de valeurs.

Il n'est pas surprenant que les entiers appartiennent au type int, les chaînes appartiennent à str et les nombres à virgule flottante à float.

Qu'en est-il des valeurs comme '2' et '42 .0 '? Ils ressemblent à des chiffres, mais ils sont en citations comme les strings.
>>> type ('2')
<classe 'str'>
>>> type ('42 .0 ')
<classe 'str'>
Ils sont des strings.

Lorsque vous tapez un grand nombre entier, vous pourriez être tenté d'utiliser des virgules entre les groupes de chiffres, soit 1 000 000. Ce n'est pas un entier juridiquement parlant en Python, mais c'est légal :

>>> 1,000,000
(1, 0, 0)
Ce n'est pas ce à quoi nous nous attendions du tout! Python interprète 1 000 000 comme une séquence d'entiers séparé par des virgules. Nous en apprendrons d’avantage sur ce genre de séquence plus tard.

1.6 Langues formelles et naturelles

Les langues sont les langues que les gens parlent, comme l'anglais, l'espagnol et le français. Ils n'étaient pas conçus par les gens (bien que les gens essayent d'imposer un ordre sur eux); ils évoluent naturellement.

Les langues formelles sont des langages conçus par des personnes pour des applications spécifiques. Par exemple, la notation utilisée par les mathématiciens est un langage formel qui est en particulier bien apte à dénoter les relations entre les nombres et les symboles. Les chimistes utilisent une langue formelle pour représenter la structure moléculaire des atomes. Et, surtout:

Les langages de programmation sont des langages formels conçus pour
exprimer les calculs.

<page 5>
1.6. Langues formelles et naturelles

Les langues formelles ont tendance à avoir des règles de syntaxe strictes qui régissent la structure des déclarations. Par exemple, en mathématiques, la déclaration 3 + 3 = 6 a une syntaxe correcte, mais 3+ = 3 $ 6 ne l’est pas. En chimie H2O est une formule syntaxiquement correcte, mais 2Zz n'est pas.

Les règles de syntaxe comportent deux saveurs, relatives aux tokens et à la structure. Les tokens sont les éléments basiques de la langue, tels que les mots, les chiffres et les éléments chimiques. Un des problèmes avec 3+ = 3 $ 6 est que $ n'est pas un token juridique en mathématiques (du moins à ce que je sais). De même, 2Zz n'est pas légal car il n'y a aucun élément avec l'abréviation Zz.

Le second type de règle de syntaxe concerne la façon dont les tokens sont combinés. L'équation 3 += 3 est illégal car même si + et = sont des tokens légaux, vous ne pouvez pas avoir un après l'autre. De même, dans une formule chimique, l'indice vient après le nom de l'élément, pas avant.

C'est une phr@se anglaise bien $tructurée avec t*kens invalide. Cette phrase valable tokens a, mais structure invalide avec.

Lorsque vous lisez une phrase en anglais ou une déclaration dans une langue officielle, vous devez identifier la structure (bien que dans une langue naturelle, vous faites cela de façon inconsciente). Ce
processus s'appelle parsing (analyse).

Bien que les langages formels et naturels possèdent de nombreuses caractéristiques communs : les token, la structure, et la syntaxe - il y a des différences:

ambiguïté: les langues naturelles sont pleines d'ambiguïté, auxquelles les gens s'occupent en utilisant des indices contextuels et d'autres informations. Les langues officielles sont conçues pour être presque ou totalement sans ambiguïté, ce qui signifie que toute déclaration a exactement un sens, quel que soit le contexte.

redondance: afin de compenser l'ambiguïté et de réduire les malentendus, les langues naturelles utilisent beaucoup de redondance. En conséquence, ils sont souvent détaillés. Les langues formelles sont moins redondantes et plus concises.

littéralité: les langues naturelles sont pleines d'idiome et de métaphore. Si je dis en anglais: "The penny dropped" (litt. le penny est tombé), il n'y a probablement pas de penny et rien n’est tombé (cette idiome signifie que quelqu'un a compris quelque chose après une période de confusion). Les langues formelles signifient exactement ce qu'ils disent. Parce que nous grandissons tous en parlant des langues naturelles, il est parfois difficile de s'adapter à la forme langues. La différence entre langage formel et naturel est comme la différence entre la poésie et la prose, mais plus encore:

Poésie: les mots sont utilisés pour leurs sons aussi bien que pour leur signification, et le poème entier ensemble crée un effet ou une réponse émotionnelle. L'ambiguïté n'est pas seulement souvent mais aussi délibéré.

Prose: le sens littéral des mots est plus important, et la structure contribue davantage au sens. La prose est plus susceptible d'analyse que le poésie, mais toujours ambiguë.

Programmes: la signification d'un programme informatique est sans ambiguïté et littérale, et peut être entièrement compris par l'analyse des tokens et de la structure.

<page 6> 
Chapitre 1. Le chemin de la programmation

Les langues formelles sont plus denses que les langues naturelles, il faut donc plus de temps pour les lire. En outre, la structure est importante, donc il n'est pas toujours préférable de lire de haut en bas, de gauche à droite. Au lieu de cela, apprenez à analyser le programme dans votre tête, identifiant les tokens et l'interprétation de la structure. Enfin, les détails sont importants. De petites erreurs dans l'orthographe et la ponctuation, dont vous pouvez vous en sortir dans des langues naturelles, peut faire une grande différence dans une langue formelle.

1.7 Débogage

Les programmeurs font des erreurs. Pour des raisons capricieuses, les erreurs de programmation sont appelées bugs et le processus de suivi est appelé débogage.
La programmation, et en particulier le débogage, soulève parfois de fortes émotions. Si vous êtes en face d’un bug difficile, vous pouvez vous sentir en colère, découragé ou embarrassé.
Il existe des preuves que les gens répondent naturellement aux ordinateurs comme s'ils étaient des gens. Quand ils fonctionnent bien, on les considère comme des coéquipiers, et quand ils sont obstinés ou grossiers, nous répondons à eux de la même manière que nous répondons à des personnes grossières et obstinées (Reeves and Nass, The Media Equation: How People Treat Computers, Television, and New Media Like Real People
and Places) .

Préparer à ces réactions pourrait vous aider à les traiter. Une approche consiste à penser à l'ordinateur en tant qu'employé avec certaines forces, comme la vitesse et la précision, et en particulier les faiblesses, comme le manque d'empathie et l'incapacité de saisir l’image en gros.

Votre travail consiste à être un bon gestionnaire: trouver des moyens de tirer parti des atouts et atténuer les faiblesses. Et trouver des façons d'utiliser vos émotions pour s'engager dans le problème, sans laisser vos réactions interférer avec votre capacité à travailler efficacement.

Apprendre à déboguer peut être frustrant, mais c'est une compétence précieuse qui est utile pour de nombreuses activités au-delà de la programmation. À la fin de chaque chapitre, il y a une section, comme celle-ci, avec
mes suggestions de débogage. J'espère qu'ils vous seront utiles!

1.8 Glossaire

résolution de problèmes / problem-solving: le processus de formulation d'un problème, la recherche d'une solution et l'exprimer.

Langage haut niveau / high-level language: un langage de programmation comme Python conçu pour être facile pour les humains à lire et à écrire.

langage de bas niveau / low-level language: un langage de programmation conçu pour être facile pour un ordinateur de parcourir; également appelé "language machine" ou "language assembly".

portabilité: une propriété d'un programme qui peut fonctionner sur plus d'un type d'ordinateur.

interprète: un programme qui lit un autre programme et l'exécute

prompt: caractères affichés par l'interprète pour indiquer qu'il est prêt à prendre une entrée de l'utilisateur.

programme: un ensemble d'instructions qui spécifient un calcul.
1.9. Exercices 
<page 7>

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

1.9 Exercices

Exercice 1.1. 
C'est une bonne idée de lire ce livre devant un ordinateur afin que vous puissiez essayer les exemples que vous allez lire.

Chaque fois que vous expérimentez avec une nouvelle fonctionnalité, vous devriez essayer de faire des erreurs. Par exemple, dans le programme «Hello World!», qu'arrive-t-il si vous laissez une des guillemets? Et qu'est-ce qui se passerait si vous quittez les deux? Que se passe-t-il si vous écrivez une mauvaise impression? Ce genre d'expérience vous aide à vous souvenir de ce que vous lisez. Cela vous aide également lorsque vous programmez, parce que vous comprenez ce que signifient les messages d'erreur. Il est préférable de faire des fautes maintenant et que plus tard et accidentellement.

1. Dans un print staement , que se passe-t-il si vous excluez l'une des parenthèses, ou les deux?

2. Si vous essayez d'imprimer une chaîne, que se passe-t-il si vous laissez une des guillemets, ou les deux?

3. Vous pouvez utiliser un signe moins pour créer un nombre négatif comme -2. Que se passe-t-il si vous mettez un + avant un nombre? Qu'en est-il de 2 ++ 2?

<page 8>
 Chapitre 1. Le chemin de la programmation

4. En notation mathématique, les zéros avancés sont corrects, comme en 02. Que se passe-t-il si vous essayez cela dans Python?

5. Que se passe-t-il si vous avez deux valeurs sans opérateur entre elles?

Exercice 1.2. Démarrez l'interpréteur Python et utilisez-le comme calculatrice.

1. Combien de secondes existe-t-il en 42 minutes 42 secondes?
2. Combien y a-t-il de miles en 10 kilomètres? Astuce: il y a 1,61 kilomètre dans un mile.
3. Si vous exécutez une course de 10 kilomètres en 42 minutes 42 secondes, quel est votre rythme moyen (temps par mile en minutes et secondes)? Quelle est votre vitesse moyenne en miles par heure?

Chapitre 2
Variables, expressions et
d�clarations

2.1 Valeurs et types

Une valeur est l'une des choses fondamentales - comme une lettre ou un chiffre - que le programme manipule. Les valeurs que nous avons vues jusqu'ici sont 2 (le r�sultat quand nous
ajout� 1 + 1), et "Hello World".
Ces valeurs appartiennent � diff�rents types: 2 est un entier, et "Hello, World!" est une cha�ne de charact�res, soi-disant parce qu'elle contient une "cha�ne" de lettres. Vous (et l'interpr�te) peut identifier les cha�nes car elles sont plac�es entre guillemets.
L'instruction print fonctionne �galement pour les entiers.
>>> print 4
4
Si vous n'�tes pas s�r du type d'une valeur, l'interpr�te peut vous le dire.
>>> type ("Bonjour, Monde!")
<type 'str'>
>>> type (17)
<type 'int'>
Sans surprise, les cha�nes appartiennent au type str et les entiers appartiennent au type int. Moins �vident, les nombres avec un point d�cimal appartiennent � un type appel� float, car ces nombres sont repr�sent�s dans un format appel� float.

>>> type (3.2)
<type 'float'>
Qu'en est-il des valeurs comme "17" et "3.2"? Ils ressemblent � des chiffres, mais ils sont
entre guillemets comme des cha�nes.
>>> type ("17")
<type 'str'>
>>> type ("3.2")
<type 'str'>
Ce sont des cha�nes de charact�res.
Lorsque vous tapez un grand entier, vous pourriez �tre tent� d'utiliser des virgules entrengroupes de trois chiffres, comme en 1.000.000 Ce n'est pas un entier l�gal en Python,
mais c'est une expression l�gale:
>>> print 1 000 000
1 0 0
Eh bien, ce n'est pas ce que nous attendions du tout! Python interpr�te 1 000 000 comme liste s�par�e par des virgules de trois entiers, qu'elle imprime cons�cutivement. C'est le premier exemple que nous avons vu d'une erreur s�mantique: le code s'ex�cute sans produisant un message d'erreur, mais il ne fait pas la "bonne" chose.

2.2 Variables

L'une des caract�ristiques les plus puissantes d'un langage de programmation est la capacit� � manipuler des variables. Une variable est un nom qui fait r�f�rence � une valeur.
L'instruction d'affectation cr�e de nouvelles variables et leur donne des valeurs:
>>> message = "Quoi de neuf, Doc?"
>>> n = 17
>>> pi = 3.14159
Cet exemple fait trois affectations. Le premier affecte la cha�ne "Quoi de neuf, Doc?"dans une nouvelle variable nomm�e message.La seconde donne l'entier 17 � n, et le troisi�me donne le nombre � virgule flottante 3.14159 � pi.
Une fa�on courante de repr�senter les variables sur papier est d'�crire le nom avec un fl�che pointant vers la valeur de la variable. Ce genre de figure est appel� un diagramme �tats-transitions car il montre dans quel �tat se situe chacune des variables (pensez-y � l'�tat d'esprit de la variable). Ce diagramme montre le r�sultat de l'affectation:
2.3 Noms de variables et mots-cl�s 13
message
n
pi
"Quoi de neuf doc?"
17
3.14159
L'instruction print fonctionne �galement avec des variables.
>>> print message
"Quoi de neuf doc?"
>>> print n
17
>>> print pi
3.14159
Dans chaque cas, le r�sultat est la valeur de la variable. Les variables ont aussi des types;
encore une fois, nous pouvons demander � l'interpr�te ce qu'ils sont.
>>> type (message)
<type 'str'>
>>> type (n)
<type 'int'>
>>> type (pi)
<type 'float'>
Le type d'une variable est le type de la valeur � laquelle elle se r�f�re.

2.3 Noms de variables et mots-cl�s

Les programmeurs choisissent g�n�ralement des noms pour leurs variables qui sont significatives - ils documentent � quoi la variable est utilis�e pour.
Les noms de variables peuvent �tre arbitrairement longs. Ils peuvent contenir � la fois des lettres et des chiffres, mais ils doivent commencer par une lettre. Bien qu'il ne soit pas intrdit d'utiliser des lettres majuscules, par convention, nous ne le faisons pas. Si vous le faites, rappelez-vous que cette affaire est importante. Bruce
et bruce sont des variables diff�rentes.
Le caract�re de soulignement () peut appara�tre dans un nom. Il est souvent utilis� dans les noms avec des mots multiples, tels que mon nom ou le prix du th� en Chine.
Si vous attribuez un nom ill�gal � une variable, vous obtenez une erreur de syntaxe:

>>> 76trombones = "grand d�fil�"
SyntaxError: invalid syntax
>>> plus $ = 1000000
SyntaxError: invalid syntax
>>> class = "Informatique 101"
SyntaxError: invalid syntax
76trombones est ill�gal car il ne commence pas par une lettre. plus $ est ill�gal parce qu'il contient un caract�re ill�gal, le signe du dollar. Mais quel est le probl�me avec class?
Il s'av�re que cette class est l'un des mots-cl�s Python. Les mots-cl�s d�finissent les r�gles et la structure du langage, et ils ne peuvent pas �tre utilis�s comme noms de variables.
Python a vingt-neuf mots-cl�s:
and def exec if not return
assert del finally import or try
break elif for in pass while
class else from is print yield
continue except global lambda raise
Vous pourriez vouloir garder cette liste � port�e de main. Si l'interpr�te se plaint d'un de vos noms de variables et vous ne savez pas pourquoi, voyez si c'est sur cette liste.

2.4 D�clarations

Une d�claration est une instruction que l'interpr�teur Python peut ex�cuter. Nous avons vu deux types d'd�clarations: print et affectations.
Lorsque vous tapez une instruction sur la ligne de commande, Python l'ex�cute et affiche le r�sultat, s'il y en a un. Le r�sultat d'une instruction print est une valeur.
Les instructions d'affectation ne produisent pas de r�sultat.
Un script contient g�n�ralement une s�quence d'instructions. S'il y en a plus d'un d�claration, les r�sultats apparaissent un � la fois.
Par exemple, le script
print 1
x = 2
print x
produit la valeur 2.5 �valuation des expressions 15
1
2
Encore une fois, l'instruction d'affectation ne produit aucun affichage.

2.5 �valuation des expressions

Une expression est une combinaison de valeurs, de variables et d'op�rateurs. Si vous tapez une expression sur la ligne de commande, l'interpr�te l'�value et affiche le r�sultat:
>>> 1 + 1
2
Bien que les expressions contiennent des valeurs, des variables et des op�rateurs, pas toutes les expressions contient tous ces �l�ments. Une valeur tout seul est consid�r�e comme expression, et est donc une variable.
>>> 17
17
>>> x
2
Etonnement, �valuer une expression n'est pas tout � fait la m�me chose que d'imprimer un valeur.
>>> message = "Quoi de neuf, Doc?"
>>> message
"Quoi de neuf doc?"
>>> print message
"Quoi de neuf doc?"
Lorsque l'interpr�teur Python affiche la valeur d'une expression, il utilise le m�me format que vous utiliseriez pour entrer une valeur. Dans le cas des cha�nes, cela signifie qu'il inclut les guillemets. Mais si vous utilisez print, Python affiche le contenu de la cha�ne sans les guillemets.
Dans un script, une expression tout seul est une d�claration l�gale, mais elle ne fait rien. Le script
17
3.2
"Bonjour le monde!"
1 + 1
ne produit aucune affichage. Comment changeriez-vous le script pour afficher les valeurs de ces quatre expressions?

2.6 Op�rateurs et op�randes

Les op�rateurs sont des symboles sp�ciaux qui repr�sentent des calculs comme l'addition et multiplication. Les valeurs utilis�es par l'op�rateur sont appel�es op�randes.
Ce qui suit sont toutes les expressions Python l�gales dont la signification est plus ou moins claire:
20 + 32 heures-1 heure * 60 + minutes minute / 60 5 ** 2 (5 + 9) * (15-7)
Les symboles +, -, et /, et l'utilisation de parenth�ses pour le regroupement signifient en Python ce qu'ils veulent dire en math�matiques. L'ast�risque (*) est le symbole de
multiplication, et ** est le symbole de l'exponentiation.
Quand un nom de variable appara�t � la place d'un op�rande, il est remplac� par sa valeur avant que l'op�ration soit effectu�e.
L'addition, la soustraction, la multiplication et l'exponentiation font toutes ce que vous attendez,
mais vous pourriez �tre surpris par la division. L'op�ration suivante a un
r�sultat inattendu:
>>> minute = 59
>>> minute / 60
0
La valeur de minute est 59, et en arithm�tique conventionnelle 59 divis� par 60 est
0,98333, pas 0. La raison de l'�cart est que Python effectue une division enti�re.
Lorsque les deux op�randes sont des entiers, le r�sultat doit �galement �tre un entier, et par convention, la division enti�re arrondit toujours vers le bas, m�me dans des cas comme celui-ci o�
l'entier suivant est tr�s proche.
Une solution possible � ce probl�me consiste � calculer un pourcentage plut�t qu'un
fraction:
>>> minute * 100/60
98
Encore une fois le r�sultat est arrondi vers le bas, mais au moins maintenant la r�ponse est environ
correct. Une autre alternative est d'utiliser la division � virgule flottante, que nous parcourerons au Chapitre 3.

2.7 Ordre des op�rations

Lorsque plus d'un op�rateur appara�t dans une expression, l'ordre d'�valuation
d�pend des r�gles de pr�s�ance. Python suit la m�me pr�s�ance
r�gles pour ses op�rateurs math�matiques que les math�matiques font. L'acronyme PEMDAS est un moyen utile de se souvenir de l'ordre des op�rations :
� Les parenth�ses ont la plus haute priorit� et peuvent �tre utilis�es pour forcer un
expression � �valuer dans l'ordre que vous voulez. Depuis les expressions entre parenth�ses
sont �valu�s en premier, 2 * (3-1) est 4, et (1 + 1) ** (5-2) est 8. Vous pouvez �galement utiliser des parenth�ses pour rendre une expression plus facile � lire, comme dans (minute * 100) / 60, m�me si cela ne change pas le r�sultat.
� L'exponentiation a la plus haute priorit� suivante, donc 2 ** 1 + 1 est 3 et non
4, et 3 * 1 ** 3 est 3 et non 27.
� La multiplication et la division ont la m�me pr�c�dence, ce qui est plus �lev�
que l'addition et la soustraction, qui ont �galement la m�me priorit�. Alors
2 * 3-1 donne 5 plut�t que 4, et 2 / 3-1 est -1, pas 1 (souvenez-vous que dans
division enti�re, 2/3 = 0).
� Les op�rateurs ayant la m�me priorit� sont �valu�s de gauche � droite. Donc dans
l'expression minute * 100/60, la multiplication arrive en premier, produisant
5900/60, ce qui donne � son tour 98. Si les op�rations avaient �t� �valu�es
de droite � gauche, le r�sultat aurait �t� 59 * 1, ce qui est 59, ce qui est faux.

2.8 Op�rations sur les cha�nes
En g�n�ral, vous ne pouvez pas effectuer d'op�rations math�matiques sur des cha�nes, m�me si
les cha�nes ressemblent � des nombres. Les �l�ments suivants sont ill�gaux (en supposant que ce message a pour type string):
message-1 "Bonjour" / 123 message * "Bonjour" "15" +2
Fait int�ressant, l'op�rateur + travaille avec des cha�nes, bien qu'il ne le fasse pas exactement ce que vous pourriez attendre. Pour les cha�nes, l'op�rateur + repr�sente la concat�nation, ce qui signifie rejoindre les deux op�randes en les reliant bout � bout. Pour
Exemple:
fruit = "banane"
bakedGood = " pain aux noix"
print fruits + bakedGood
Le r�sultat de ce programme est "banane pain aux noix". L'espace avant le mot noix fait partie de la cha�ne, et est n�cessaire pour produire l'espace entre le cha�nes concat�n�es.
L'op�rateur * travaille �galement sur les cha�nes; il effectue la r�p�tition. Par exemple,
"Fun" * 3 est "FunFunFun". L'un des op�randes doit �tre une cha�ne; l'autre doit �tre un nombre entier.

D'une part, cette interpr�tation de + et * a un sens par analogie avec l'addition et multiplication. Tout comme 4 * 3 �quivaut � 4 + 4 + 4, nous nous attendons � ce que "Fun" * 3
�tre le m�me que "Fun" + "Fun" + "Fun", et il est. D'un autre c�t�, il y a un fa�on significative dans laquelle la concat�nation de cha�nes et la r�p�tition sont diff�rentes de addition et multiplication enti�res. Pouvez-vous penser � une propri�t� que l'addition
et la multiplication ont et que la concat�nation et la r�p�tition n'ont pas?

2.9 Composition

Jusqu'� pr�sent, nous avons examin� les �l�ments d'un programme-variables, expressions,et d�clarations - isol�ment, sans parler de la fa�on de les combiner.
L'une des caract�ristiques les plus utiles des langages de programmation est leur capacit� � prendre de petits blocs de construction et de les composer. Par exemple, nous savons comment ajouter des chiffres et nous savons comment imprimer; il se trouve que nous pouvons faire les deux � la fois :
>>> print 17 + 3
20
En r�alit�, l'ajout doit se produire avant l'impression, de sorte que les actions ne sont pas
se passe r�ellement en m�me temps. Le fait est que toute expression impliquant les nombres, les cha�nes et les variables peuvent �tre utilis�s dans une instruction print. Vous avez
d�j� vu un exemple de ceci:
print "Nombre de minutes �coul�es depuis minuit:", heure * 60 + minute
Vous pouvez �galement placer des expressions arbitraires sur le c�t� droit d'une affectation :
pourcentage = (minute * 100) / 60
Cette capacit� peut ne pas sembler impressionnante maintenant, mais vous verrez d'autres exemples
o� la composition permet d'exprimer des calculs complexes
et concise.
Attention: Il y a des limites sur l'endroit o� vous pouvez utiliser certaines expressions. Par exemple,
le c�t� gauche d'une instruction d'affectation doit �tre un nom de variable,
pas une expression. Donc, ce qui suit est ill�gal: minute + 1 = heure.

2.10 Commentaires

� mesure que les programmes deviennent plus gros et plus compliqu�s, ils deviennent plus difficiles � lire.
Les langages formels sont denses, et il est souvent difficile de regarder un morceau de code
et comprendre ce qu'il fait, ou pourquoi.

Pour cette raison, c'est une bonne id�e d'ajouter des notes � vos programmes pour expliquer dans
langage naturel ce que le programme fait. Ces notes sont appel�es commentaires,
et ils sont marqu�s du symbole #:
# calcule le pourcentage de l'heure qui s'est �coul�e
pourcentage = (minute * 100) / 60
Dans ce cas, le commentaire appara�t sur une ligne par lui-m�me. Vous pouvez �galement mettre des commentaires
� la fin d'une ligne:
pourcentage = (minute * 100) / 60 # attention: division enti�re
Tout du # � la fin de la ligne est ignor� - il n'a aucun effet sur le
programme. Le message est destin� au programmeur ou aux futurs programmeurs
qui pourrait utiliser ce code. Dans ce cas, il rappelle au lecteur le
comportement toujours surprenant de la division enti�re.
Ce genre de commentaire est moins n�cessaire si vous utilisez l'op�ration de division enti�re,
//. Il a le m�me effet que l'op�rateur de division1
, mais cela indique que l'effet est d�lib�r�.
pourcentage = (minute * 100) // 60
L'op�rateur de division entier est comme un commentaire qui dit: "Je sais que c'est un nombre entier
division, et je l'aime comme �a! "

2.11 Glossaire

value: Un nombre ou une cha�ne (ou une autre chose � nommer plus tard) qui peut �tre stock�e dans une variable ou calcul� dans une expression.
type: un ensemble de valeurs. Le type d'une valeur d�termine comment elle peut �tre utilis�e dans les expressions. Jusqu'� pr�sent, les types que vous avez vus sont des entiers (type int), nombres flottants (type float) et cha�nes (type string).
floating-point: Un format pour repr�senter des nombres avec des parties fractionnaires.
variable: un nom qui fait r�f�rence � une valeur.
statement: Une section de code repr�sentant une commande ou une action. Jusqu'� pr�sent, les d�clarations que vous avez vues sont des affectations et des d�clarations print.
affectation: une instruction qui affecte une valeur � une variable.
1Pour maintenant. Le comportement de l'op�rateur de division peut changer dans les futures versions de Python.
20 Variables, expressions et d�clarations 
state diagrams: Repr�sentation graphique d'un ensemble de variables et des valeurs
auquel ils se r�f�rent.
keyword : mot r�serv� utilis� par le compilateur pour analyser un programme;
vous ne pouvez pas utiliser des mots-cl�s comme if, def et while comme noms de variables.
operator: Un symbole sp�cial qui repr�sente un calcul simple comme l'addition,
multiplication, ou concat�nation de cha�ne.
Op�rande: Une des valeurs sur lesquelles un op�rateur op�re.
expression: une combinaison de variables, d'op�rateurs et de valeurs repr�sentant
une seule valeur de r�sultat.
�valuer: Pour simplifier une expression en effectuant les op�rations afin de
donner une seule valeur.
division enti�re: Op�ration qui divise un entier par un autre et donne
un nombre entier. La division enti�re ne donne que le nombre entier de fois que
Le num�rateur est divisible par le d�nominateur et rejette tout ce qui reste.
r�gles de pr�c�dance: Ensemble de r�gles r�gissant l'ordre dans lequel les expressions impliquant plusieurs op�rateurs et op�randes sont �valu�s.
concat�ner: Pour combiner deux op�randes.
composition: La capacit� de combiner des expressions simples et des d�clarations dans
expressions et expressions compos�es afin de repr�senter des calculs complexes
avec concision.
commentaire : Information dans un programme destin� � d'autres programmeurs (ou quiconque lit le code source) et n'a aucun effet sur l'ex�cution du programme.chapitre 3
Les fonctions

3.1 Appels de fonction

Vous avez déjà vu un exemple d'appel de fonction:
>>> type ("32")
<type 'str'>
Le nom de la fonction est type, et il affiche le type d'une valeur ou d'une variable.
La valeur ou variable, appelée argument de la fonction, doit
être entouré de parenthèses. Il est courant de dire qu'une fonction "prend" un
argument et "renvoie" un résultat. Le résultat est appelé la valeur de retour.
Au lieu d'imprimer la valeur de retour, nous pourrions l'assigner à une variable:
>>> betty = type ("32")
>>> print betty
<type 'str'>
Comme un autre exemple, la fonction id prend une valeur ou une variable et retourne un
entier qui agit comme un identifiant unique pour la valeur:
>>> id (3)
134882108
>>> betty = 3
>>> id (betty)
134882108
Chaque valeur a un identifiant, qui est un nombre unique lié à l'endroit où il est stocké
dans la mémoire de l'ordinateur. L'identifiant d'une variable est l'identifiant de la valeur à
auquel il se réfère.

3.2 Conversion de type

Python fournit une collection de fonctions intégrée qui convertit les valeurs d'un
int à un autre. La fonction int prend n'importe quelle valeur et la convertit en entier,
si possible, ou se plaint autrement:
>>> int ("32")
32
>>> int ("Bonjour")
ValueError: invalid literal for int(): Hello
int peut également convertir des floats en entiers, mais rappelez-vous qu'il
tronque la partie fractionnaire:
>>> int (3.99999)
3
>>> int (-2.3)
-2
La fonction float convertit les entiers et les chaînes en float:
>>> float (32)
32,0
>>> float ("3.14159")
3.14159
Enfin, la fonction str convertit en chaîne de caractères:
>>> str (32)
'32'
>>> str (3.14149)
'3.14149'
Il peut sembler étrange que Python distingue la valeur entière 1 du float 
1,0. Ils peuvent représenter le même nombre, mais ils appartiennent à
différents types. La raison en est qu'ils sont représentés différemment dans
l'ordinateur.

3.3 Coertion de type

Maintenant que nous pouvons convertir entre les types, nous avons une autre façon de faire face à
la division entière. En revenant à l'exemple du chapitre précédent, supposons que
nous voulons calculer la fraction d'une heure qui s'est écoulée. Le plus évident
expression, minute / 60, fait l'arithmétique entière, donc le résultat est toujours 0, même
à 59 minutes après l'heure.

Une solution consiste à convertir la minute en float et faire la division:
>>> minute = 59
>>> float (minute) / 60
0,983333333333
Alternativement, nous pouvons tirer parti des règles pour la conversion automatique de type,
ce qui s'appelle la coercition de type. Pour les opérateurs mathématiques, si
l'opérande est un float, l'autre est automatiquement converti en un float:
>>> minute = 59
>>> minute / 60.0
0,983333333333
En transformant le dénominateur en float, nous forçons Python à faire la division comme on souhaitait.

3.4 Fonctions mathématiques

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
>>> import math
Pour appeler l'une des fonctions, nous devons spécifier le nom du module et le
nom de la fonction, séparé par un point, également appelé période. Ce format
est appelée dot notation.

>>> decibel = math.log10 (17.0)
>>> angle = 1.5
>>> height = math.sin (angle)
La première déclaration définit le décibel au logarithme de 17, base 10. Il y a aussi
une fonction appelée log qui prend logarithme base e.
La troisième déclaration trouve le sinus de la valeur de l'angle variable.Sin et
les autres fonctions trigonométriques (cos, tan, etc.) prennent des arguments en radian.
Pour convertir des degrés en radians, diviser par 360 et multiplier par 2 * pi. Pour
par exemple, pour trouver le sinus de 45 degrés, d'abord calculer l'angle en radians et
alors prenez le sinus:
>>> degrees = 45
>>> angle = degrés * 2 * math.pi / 360.0
>>> math.sin (angle)
0,707106781187
La constante pi fait également partie du module mathématique. Si vous connaissez votre géométrie,
vous pouvez vérifier le résultat précédent en le comparant à la racine carrée de deux
divisé par deux:
>>> math.sqrt (2) / 2.0
0,707106781187

3.5 Composition

Tout comme avec les fonctions mathématiques, les fonctions Python peuvent être composées, ce qui signifie
que vous utilisez une expression dans le cadre d'une autre. Par exemple, vous pouvez utiliser
toute expression en tant qu'argument à une fonction:
>>> x = math.cos (angle + math.pi / 2)
Cette instruction prend la valeur de pi, la divise par 2 et ajoute le résultat à
;a valeur de l'angle. La somme est ensuite passée en argument à la fonction cos.
Vous pouvez également prendre le résultat d'une fonction et le passer en argument
un autre:
>>> x = math.exp (math.log (10.0))
Cette instruction trouve la base de log e de 10, puis augmente e à cette puissance. le
le résultat est assigné à x.

3.6 Ajout de nouvelles fonctions

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
def NOM (LISTE DES PARAMETRES):
	DECLARATIONS
Vous pouvez choisir les noms que vous voulez pour les fonctions que vous créez, sauf que
vous ne pouvez pas utiliser un nom qui est un mot clé Python. La liste des paramètres spécifie
quelles informations, le cas échéant, vous devez fournir pour utiliser la nouvella fonction.
Il peut y avoir un certain nombre d'instructions à l'intérieur de la fonction, mais elles doivent
être en retrait de la marge de gauche. Dans les exemples de ce livre, nous utiliserons un
indentation de deux espaces.
Le premier couple de fonctions que nous allons écrire n'a pas de paramètres, de sorte que le
la syntaxe ressemble à ceci:
def nouvelleLigne():
	print
Cette fonction s'appelle nouvelleLigne. Les parenthèses vides indiquent qu'il n'a
pas de paramètres. Il contient seulement une seule instruction, qui génère une nouvelle ligne
(C'est ce qui se passe lorsque vous utilisez une commande print sans aucun
arguments.)
La syntaxe d'appel de la nouvella fonction est la même que celle de la fonction intégrée
les fonctions:
print "Premiere ligne"
nouvelleLigne()
print "Deuxieme ligne"
La sortie de ce programme est:
Premiere ligne.

Deuxieme ligne.
Notez l'espace supplémentaire entre les deux lignes. Et si nous voulions plus d'espace
entre les lignes? Nous pourrions appeler la même fonction à plusieurs reprises:
print "Premiere ligne"
nouvelleLigne()
nouvelleLigne()
nouvelleLigne()
print "Deuxieme ligne"
Nous pourrions écrire une nouvella fonction appelée trois lignes qui imprime trois nouveaux
lignes:
def troisLignes():
	nouvelleLigne()
	nouvelleLigne()
	nouvelleLigne()
print "Premiere ligne"
troisLignes()
print "Deuxieme ligne"
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

3.7 Définitions et utilisation

• Créer une nouvella fonction peut réduire la taille d'un programme en éliminant les répétitions.
Par exemple, un court chemin pour imprimer neuf nouvelles lignes consécutives
est d'appeler troisLignes trois fois.
Comme un exercice, écrivez une fonction appelée neufLignes qui utilise
troisLignes pour imprimer neuf lignes vides. Comment voulez-vous imprimer vingt-sept
nouvelles lignes?
En rassemblant les fragments de code de la section 3.6, l'ensemble du programme semble
comme cela:
def nouvelleLigne ():
	print
def troisLignes ():
	nouvelle ligne()
	nouvelle ligne()
	nouvelle ligne()
print "Premiere ligne"
troisLignes ()
print "Deuxieme ligne"
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

3.8 Flux d'exécution

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

3.9 Paramètres et arguments

Certaines des fonctions intégrées que vous avez utilisées nécessitent des arguments, les valeurs qui
contrôlent comment la fonction fait son travail. Par exemple, si vous voulez trouver le
sinus d'un nombre, vous devez indiquer quel est le nombre. Ainsi, sin prend un
valeur numérique en tant qu'argument.
Certaines fonctions prennent plus d'un argument. Par exemple, pow prend deux
arguments, la base et l'exposant. Dans la fonction, les valeurs passées qui
sont affectées à des variables appelées paramètres.
Voici un exemple de fonction définie par l'utilisateur qui a un paramètre:
def printDouble(bruce):
	print bruce, bruce
Cette fonction prend un seul argument et l'affecte à un paramètre nommé
bruce. La valeur du paramètre (à ce stade, nous n'avons aucune idée de ce que cela va
être) est imprimé deux fois, suivi d'une nouvelle ligne. Le nom bruce a été choisi pour
suggérer que le nom que vous donnez un paramètre est à vous, mais en général, vous
voulez choisir quelque chose de plus illustratif que Bruce.
La fonction printDoubla fonctionne pour tous les types qui peuvent être imprimés:
>>> printDouble ('Spam')
Spam Spam
>>> printDouble (5)
5 5
>>> printDouble (3.14159)
3.14159 3.14159
Dans le premier appel de fonction, l'argument est une chaîne. Dans la seconde, c'est un nombre entier.
Dans le troisième, c'est un float.
Les mêmes règles de composition qui s'appliquent aux fonctions intégrées s'appliquent également aux
fonctions définies par l'utilisateur, de sorte que nous pouvons utiliser n'importe quel type d'expression comme argument de
printDouble:
>>> printDouble ('Spam' * 4)
SpamSpamSpamSpam SpamSpamSpamSpam
>>> printDouble (math.cos (math.pi))
-1,0 -1,0
Comme d'habitude, l'expression est évaluée avant l'exécution de la fonction, donc printDouble
imprime SpamSpamSpamSpam SpamSpamSpamSpam au lieu de 'Spam' * 4 'Spam' * 4.
Comme exercice, écrivez un appel à printDouble qui imprime 'Spam' * 4
'Spam' * 4. Astuce: les cordes peuvent être enfermées en simple ou en double
guillemets, et le type de citation non utilisé pour entourer la chaîne peut être
utilisé à l'intérieur comme une partie de la chaîne.
Nous pouvons également utiliser une variable comme argument:
>>> michael = 'Eric, la demi-abeille.'
>>> printDouble (michael)
Eric, la demi-abeille. Eric, la demi-abeille.
Remarquez quelque chose de très important ici. Le nom de la variable que nous transmettons
argument (michael) n'a rien à voir avec le nom du paramètre (bruce).
Peu importe ce que la valeur a été rappelée à la maison (dans l'appelant); ici dans
printDouble, nous appelons tout le monde bruce.

3.10 Les variables et les paramètres locaux

Lorsque vous créez une variable locale à l'intérieur d'une fonction, elle n'existe que dans la
fonction, et vous ne pouvez pas l'utiliser à l'extérieur. Par exemple:
def chatDouble (partie1, partie2):
	chat = partie1 + partie2
	printDouble (chat)
Cette fonction prend deux arguments, les concatène, puis imprime le
résultat deux fois. Nous pouvons appeler la fonction avec deux chaînes:
>>> chant1 = "Pie Jesu domine"
>>> chant2 = "Dona eis requiem."
>>> chatDouble (chant1, chant2)
Pie Jesu domine, Dona eis requiem. Pie Jesu domine, Dona eis requiem.
Lorsque chatDouble se termine, la variable chat est détruite. Si nous essayons de l'imprimer,
nous avons une erreur:
>>> print chat
NameError: chat
Les paramètres sont également locaux. Par exemple, en dehors de la fonction printDouble, il y n'y a
pa une telle chose que bruce. Si vous essayez de l'utiliser, Python va se plaindre.

3.11 Diagrammes de pile / stack diagram

Pour garder une trace des variables qui peuvent être utilisées où, il est parfois utile de
dessiner un diagramme de pile. Comme les diagrammes d'état, les diagrammes de pile montrent la valeur de
chaque variable, mais ils montrent également la fonction à laquelle chaque variable appartient.
Chaque fonction est représentée par un cadre. Un cadre est une boîte avec le nom de
fonction à côté d'elle et les paramètres et les variables de la fonction à l'intérieur.
Le diagramme de pile de l'exemple précédent ressemble à ceci:

[DIAGRAM HERE]

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
NameError:
Traceback (innermost last):
	File "test.py", ligne 13, in __main__
	chatDouble (chant1, chant2)
	File "test.py", ligne 5, in chatDouble
	printDouble (chat)
	File "test.py", ligne 9, in printDouble
	print chat
NameError: chat
Cette liste de fonctions est appelée traceback. Il vous indique dans quel fichier de programme
l'erreur s'est produite, et quelle ligne, et quelles fonctions étaient en cours d'exécution à ce moment.
Il montre également la ligne de code qui a provoqué l'erreur.
Notez la similarité entre le traceback et le diagramme de pile. Ce n'est pas un
coïncidence.

3.12 Fonctions avec résultats

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

3.13 Glossaire

function call / appel de fonction: une instruction qui exécute une fonction. Il se compose du nom
de la fonction suivie d'une liste d'arguments entre parenthèses.
argument: Une valeur fournie à une fonction lorsque la fonction est appelée. Ce
La valeur est affectée au paramètre correspondant dans la fonction.
return value: Le résultat d'une fonction. Si un appel de fonction est utilisé comme une expression,
la valeur de retour est la valeur de l'expression.
type conversion: Une instruction explicite qui prend une valeur d'un type et
calcule une valeur correspondante d'un autre type.
coercition de type: Une conversion de type qui se produit automatiquement selon
les règles de coercition de Python.
module: un fichier qui contient une collection de fonctions et de classes associées.
dot notation: La syntaxe pour appeler une fonction dans un autre module, en spécifiant
le nom du module suivi d'un point (periode) et du nom de la fonction.
function: Une séquence nommée d'instructions qui effectue une opération utile.
Les fonctions peuvent ou non prendre des arguments et peuvent ou non
produire un résultat.
définition de fonction: une instruction qui crée une nouvelle fonction, en spécifiant sa
nom, les paramètres et les instructions qu'il exécute.
flux d'exécution: ordre dans lequel les instructions sont exécutées pendant un programme
courir.
paramètre: Un nom utilisé dans une fonction pour faire référence à la valeur passée en tant que
argument.
variable locale: Une variable définie à l'intérieur d'une fonction. Une variable locale peut seulement
être utilisé à l'intérieur de sa fonction.
diagramme de pile: représentation graphique d'une pile de fonctions, leurs variables,
et les valeurs auxquelles ils se réfèrent.
frame: Une boîte dans un diagramme de pile qui représente un appel de fonction. Il contient
les variables locales et les paramètres de la fonction.
traceback: une liste des fonctions en cours d'exécution, imprimées lors d'une exécution
erreur se produit.Chapitre 4

Etude de cas: conception d'interface
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

4.1

Le module tortue

Pour vérifier si vous avez le module tortue, ouvrez l'interpréteur Python et tapez

>>> import turtle
>>> bob = turtle.Turtle()
Lorsque vous exécutez ce code, il doit créer une nouvelle fenêtre avec une petite flèche qui représente
la tortue. Fermez la fenêtre.
Créez un fichier nommé mypolygon.py et tapez le code suivant:

import turtle
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
Le module turtle (avec un 't' minuscule) fournit une fonction appelée Turtle (avec un 'T' majuscule) qui crée un objet Turtle, que nous assignons à une variable nommée bob. print
bob affiche quelque chose comme:

<turtle.Turtle object at 0xb7bfbf4c>

30

Chapitre 4. Etude de cas: conception d'interface

Cela signifie que bob fait référence à un objet de type Turtle tel que défini dans la tortue de module.

mainloop indique à la fenêtre d'attendre que l'utilisateur fasse quelque chose, bien que dans ce cas
il n'y a pas grand chose à faire pour l'utilisateur, sauf fermer la fenêtre.
Une fois que vous créez une tortue, vous pouvez appeler une méthode pour la déplacer dans la fenêtre. Une méthode
est similaire à une fonction, mais utilise une syntaxe légèrement différente. Par exemple, pour déplacer la tortue
vers l'avant:

bob.fd (100)
La méthode, fd, est associée à l'objet tortue que nous appelons bob. L'appel d'une méthode est
comme faire une demande: vous demandez à Bob d'avancer.
L'argument de fd étant une distance en pixels, la taille réelle dépend de votre affichage.
Les autres méthodes que vous pouvez appeler sur une tortue sont bk pour reculer, lt pour tourner à gauche et rt
virage à droite. L'argument pour lt et rt est un angle en degrés.
En outre, chaque tortue tient un stylo, qui est soit en bas soit en haut; si le stylo est en panne, la tortue
laisse une trace quand il bouge. Les méthodes pu et pd représentent "pen up" et "pen down".
Pour dessiner un angle droit, ajoutez ces lignes au programme (après avoir créé bob et avant d'appeler la
boucle principale):

bob.fd (100)
bob.lt (90)
bob.fd (100)
Lorsque vous exécutez ce programme, vous devriez voir Bob se déplacer vers l’est puis vers le nord, laissant deux
segments de ligne derrière.
Modifiez maintenant le programme pour dessiner un carré. Ne continuez pas tant que vous ne l'avez pas fait fonctionner!

4.2

Répétition simple

Les chances sont que vous avez écrit quelque chose comme ceci:

bob.fd (100)
bob.lt (90)
bob.fd (100)
bob.lt (90)
bob.fd (100)
bob.lt (90)
bob.fd (100)
Nous pouvons faire la même chose de manière plus concise avec une déclaration. Ajouter cet exemple à
mypolygon.py et lancez-le à nouveau:

for i in range(4):
print('Hello!')
Vous devriez voir quelque chose comme ceci:

4.3. Exercices

31

Hello!
Hello!
Hello!
Hello!
C'est l'utilisation la plus simple de la déclaration for; nous verrons plus tard. Mais cela devrait être
de quoi vous permettre de réécrire votre programme de dessin en carré. Ne continuez pas jusqu'à ce que vous fassiez.
Voici une déclaration qui dessine un carré:
for i in range(4):
bob.fd(100)
bob.lt(90)
La syntaxe d'une instruction for est similaire à une définition de fonction. Il a un en-tête qui se termine
avec un colon et un corps en retrait. Le corps peut contenir n'importe quel nombre d'instructions.
Un déclaration for est également appelé une boucle parce que le flux d'exécution traverse le corps
puis retourne au sommet. Dans ce cas, il court le corps quatre fois.
Cette version est en fait un peu différente du précédent code de dessin car
fait un autre tour après avoir dessiné le dernier côté de la place. Le tour supplémentaire prend plus
temps, mais cela simplifie le code si nous faisons la même chose à chaque fois dans la boucle. Ce
version la a également pour effet de laisser la tortue dans la position de départ, face à la
direction de départ.

4.3

Exercices

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

32

4.4

Chapitre 4. Etude de cas: conception d'interface

Encapsulation

Le premier exercice vous demande de mettre votre code de dessin carré dans une définition de fonction et
puis appelez la fonction, en passant la tortue en paramètre. Voici une solution:

def square(t):
for i in range(4):
t.fd(100)
t.lt(90)
square(bob)
Les instructions les plus internes, fd et lt, sont en retrait deux fois pour montrer qu'elles sont à l'intérieur du
for loop, qui se trouve dans la définition de la fonction. La ligne suivante, square (bob), est alignée avec
la marge de gauche, qui indique la fin de la boucle for et la définition de la fonction.
À l’intérieur de la fonction, t fait référence au même bob tortue, donc t.lt (90) a le même effet que
bob.lt (90). Dans ce cas, pourquoi ne pas appeler le paramètre bob? L'idée est que t peut être n'importe quel
tortue, pas seulement bob, vous pouvez donc créer une deuxième tortue et la passer en argument

alice = turtle.Turtle()
square(alice)
L'encapsulation d'un morceau de code dans une fonction est appelée encapsulation. Un des avantages de
l'encapsulation consiste à attacher un nom au code, qui sert de type de documentation. Un autre avantage est que si vous réutilisez le code, il est plus concis d'appeler une fonction
deux fois que de copier et coller le corps!

4.5

Généralisation

L'étape suivante consiste à ajouter un paramètre de longueur à square. Voici une solution:

def square(t, length):
for i in range(4):
t.fd(length)
t.lt(90)
square(bob, 100)
L'ajout d'un paramètre à une fonction s'appelle la généralisation car elle fait la fonction
plus général: dans la version précédente, le carré a toujours la même taille; dans cette version c'est
peut être n'importe quelle taille.
L'étape suivante est également une généralisation. Au lieu de dessiner des carrés, le polygone dessine des
polygones régulière avec un nombre quelconque de côtés. Voici une solution:

def polygon(t, n, length):
angle = 360 / n
for i in range(n):
t.fd(length)
t.lt(angle)
polygon(bob, 7, 70)

4.6. Design d'interface

33

Cet exemple dessine un polygone à sept côtés avec une longueur de côté 70.
Si vous utilisez Python 2, la valeur de l'angle peut être désactivée en raison de la division entière. Une
solution simple est de calculer l’angle = 360.0 / n. Le numérateur étant un nombre à virgule flottante, le résultat est un nombre à virgule flottante.
Lorsqu'une fonction a plus que quelques arguments numériques, il est facile d'oublier ce qu'ils sont,
ou dans quel ordre ils devraient être. Dans ce cas, il est souvent utile d'inclure les noms de
les paramètres de la liste d'arguments:

polygon(bob, n=7, length=70)
Ceux-ci sont appelés des arguments de mots-clés car ils incluent les noms de paramètres en tant que "mots-clés" (à ne pas confondre avec les mots-clés Python comme while et def).
Cette syntaxe rend le programme plus lisible. C'est aussi un rappel sur la façon dont les arguments
et paramètres fonctionnent: lorsque vous appelez une fonction, les arguments sont affectés aux paramètres.

4.6

Design d'interface

L'étape suivante consiste à écrire le cercle, qui prend un rayon, r, en tant que paramètre. Voici un simple
solution qui utilise un polygone pour dessiner un polygone à 50 côtés:

import math
def circle(t, r):
circumference = 2 * math.pi * r
n = 50
length = circumference / n
polygon(t, n, length)
longueur = circonférence / n
polygone (t, n, longueur)
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

34

Chapitre 4. Etude de cas: conception d'interface

def circle(t, r):
circumference = 2 * math.pi * r
n = int(circumference / 3) + 3
length = circumference / n
polygon(t, n, length)
Maintenant, le nombre de segments est un entier proche de la circumference/3, donc la longueur de chaque
le segment est d'environ 3, ce qui est assez petit pour que les cercles semblent bons, mais gros
suffisamment pour être efficace et acceptable pour tout cercle de taille.
L'ajout de 3 à n garantit que le polygone a au moins 3 côtés.

4.7

Refactoring

Lorsque j'ai écrit le cercle, j'ai pu réutiliser un polygone car un polygone à plusieurs côtés est un bon
approximation d'un cercle. Mais l'arc n'est pas aussi coopératif; nous ne pouvons pas utiliser polygone ou cercle pour
dessine un arc.
Une alternative consiste à commencer par une copie du polygone et à le transformer en arc. Le résultat
pourrait ressembler à ceci:

def arc(t, r, angle):
arc_length = 2 * math.pi * r * angle / 360
n = int(arc_length / 3) + 1
step_length = arc_length / n
step_angle = angle / n
for i in range(n):
t.fd(step_length)
t.lt(step_angle)
La seconde moitié de cette fonction ressemble à un polygone, mais nous ne pouvons pas réutiliser un polygone sans
changer l'interface. On pourrait généraliser le polygone pour prendre un angle comme troisième argument,
mais alors le polygone ne serait plus un nom approprié! Au lieu de cela, appelons le plus
fonction générale polyligne:
def polyline(t, n, length, angle):
for i in range(n):
t.fd(length)
t.lt(angle)
Maintenant, nous pouvons réécrire le polygone et l'arc pour utiliser la polyligne:
def polygon(t, n, length):
angle = 360.0 / n
polyline(t, n, length, angle)
def arc(t, r, angle):
arc_length = 2 * math.pi * r * angle / 360
n = int(arc_length / 3) + 1
step_length = arc_length / n
step_angle = float(angle) / n
polyline(t, n, step_length, step_angle)
Enfin, nous pouvons réécrire le cercle pour utiliser l'arc:

4.8. Un plan de développement

35

def circle(t, r):
arc(t, r, 360)
Ce processus de réorganisation d'un programme pour améliorer les interfaces et faciliter la réutilisation du code est
appelé refactoring. Dans ce cas, nous avons remarqué qu'il y avait un code similaire en arc et en polygone,
donc nous avons "factorisé" en polyligne.
Si nous avions prévu à l’avance, nous aurions peut-être écrit la polyligne d’abord et évité la refactorisation,
mais souvent vous ne savez pas assez au début d'un projet pour concevoir toutes les interfaces.
Une fois que vous commencez à coder, vous comprenez mieux le problème. Parfois, le refactoring est un signe
que vous avez appris quelque chose.

4.8

Un plan de développement

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

4.9

docstring

Un docstring est une chaîne au début d'une fonction qui explique l'interface ("doc" est
abréviation de "documentation"). Voici un exemple:

def polyline(t, n, length, angle):
"""Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
for i in range(n):
t.fd(length)
t.lt(angle)
Par convention, toutes les chaînes de caractères sont des chaînes entre guillemets, également appelées chaînes multilignes.
car les triples guillemets permettent à la chaîne de s'étendre sur plusieurs lignes.

36

Chapitre 4. Etude de cas: conception d'interface

C'est concis, mais il contient l'information essentielle dont quelqu'un aurait besoin pour utiliser cette fonction. Il explique de manière concise ce que la fonction fait (sans entrer dans les détails de la façon dont
il le fait). Il explique quel effet chaque paramètre a sur le comportement de la fonction et
quel type chaque paramètre devrait être (si ce n'est pas évident).
L'écriture de ce type de documentation est une partie importante de la conception de l'interface. Une interface bien conçue devrait être simple à expliquer; si vous avez du mal à en expliquer un
de vos fonctions, peut-être l'interface pourrait être améliorée.

4.10

Le débogage

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

4.11

Glossaire

method: Fonction associée à un objet et appelée à l'aide de la notation par points.
loop: Partie d'un programme pouvant être exécutée à plusieurs reprises.
encapsulation: processus de transformation d'une séquence d'instructions en une définition de fonction.
généralisation: processus de remplacement de quelque chose d'inutile (comme un nombre)
avec quelque chose de façon générale (comme une variable ou un paramètre).
keyword argument: argument qui inclut le nom du paramètre en tant que "mot-clé".
interface: description de l'utilisation d'une fonction, y compris le nom et les descriptions de
les arguments et la valeur de retour.
refactoring: Processus de modification d'un programme de travail pour améliorer les interfaces de fonction
et d'autres qualités du code.
plan de développement: Un processus pour écrire des programmes.

4.12. Des exercices

37

Figure 4.1: Fleurs de tortue.

Figure 4.2: Tartes aux tortues.
docstring: Chaîne qui apparaît en haut d'une définition de fonction pour documenter l'interface de la fonction.
condition préalable: exigence qui doit être satisfaite par l'appelant avant le démarrage d'une fonction.
postcondition: Une exigence qui devrait être satisfaite par la fonction avant sa fin.

4.12

Des exercices

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

38

Chapitre 4. Etude de cas: conception d'interface

Vous pouvez obtenir une solution à partir de http: // thinkpython2. com / code / lettres. py; il faut aussi
http: // thinkpython2. com / code / polygone. py.
Exercice 4.5. Lisez à propos des spirales sur http: // fr. Wikipedia. org / wiki / Spiral; puis écrire
un programme qui dessine une spirale archimédienne (ou l'une des autres sortes). Solution: http:
// thinkpython2. com / code / spirale. py.Chapitre 5

Conditions et récursivité
Le sujet principal de ce chapitre est l'instruction if, qui exécute un code différent en fonction de
l'état du programme. Mais je veux d'abord présenter deux nouveaux opérateurs: la division floor et
le modulus.

5.1

Division et module de plancher

L'opérateur de division floor, //, divise deux nombres et arrondit à un entier. Par
exemple, supposons que le temps d'exécution d'un film est de 105 minutes. Vous voudrez peut-être savoir le temps
en heures. La division conventionnelle renvoie un nombre à virgule flottante:

>>> minutes = 105
>>> minutes / 60
1.75
Mais normalement, nous n'écrivons pas des heures avec des points décimaux. La division d'étage renvoie le nombre d'heures
en entier, en laissant tomber la fraction:

>>> minutes = 105
>>> hours = minutes // 60
>>> hours
1
Pour obtenir le reste, vous pouvez soustraire une heure en minutes:

>>> remainder = minutes - hours * 60
>>> remainder
45
Une alternative consiste à utiliser l'opérateur de modulus,%, qui divise deux nombres et renvoie
le reste.

>>> remainder = minutes % 60
>>> remainder
45
L'opérateur modulus est plus utile qu'il n'y paraît. Par exemple, vous pouvez vérifier si
un nombre est divisible par un autre - si x% y est zéro, alors x est divisible par y.

40

Chapitre 5. Conditions et récursivité

Vous pouvez également extraire le chiffre ou les chiffres les plus à droite d'un nombre. Par exemple, x%10
donne le chiffre le plus à droite de x (en base 10). De même, x%100 fournit les deux derniers chiffres.
Si vous utilisez Python 2, la division fonctionne différemment. L'opérateur de division, /, effectue
la division de plancher si les deux opérandes sont des nombres entiers, et la division en virgule flottante si l'un des opérandes est
un flotteur.

5.2

Expressions booléennes

Une expression booléenne est une expression vraie ou fausse. Les exemples suivants
utilisent l'opérateur ==, qui compare deux opérandes et produit True s'ils sont égaux
et False sinon:

>>> 5 == 5
True
>>> 5 == 6
False
True et False sont des valeurs spéciales appartenant au type bool; ce ne sont pas des strings:
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
L'opérateur == est l'un des opérateurs relationnels; les autres sont:

X
X
X
X
X

! = y
> y
<y
> = y
<= y

#
#
#
#
#

X
X
X
X
X

is
is
is
is
is

pas égal à
plus grand que
moins que y
plus grand que
moins que ou

y
y
ou égal à y
égal à y

Bien que ces opérations vous soient probablement familières, les symboles Python sont différents
des symboles mathématiques. Une erreur courante consiste à utiliser un seul signe égal (=) au lieu d'un
double signe égal (==). Rappelez-vous que = est un opérateur d'affectation et == est un opérateur
relationnel. Il n'y a pas de chose comme =< ou =>.

5.3

Opérateurs logiques

Il existe trois opérateurs logiques: et, ou, et non. La sémantique (signification) de ces
opérateurs sont similaires à leur signification en anglais. Par exemple, x>0 et x<10 est vrai
seulement si x est supérieur à 0 et inférieur à 10.

n%2 == 0 ou n%3 == 0 est vrai si l’une ou les deux conditions est vraie, c’est-à-dire si le nombre
est divisible par 2 ou 3.
Enfin, l’opérateur not nie une expression booléenne, donc pas (x>y) est vrai si x>y est
False, c'est-à-dire si x est inférieur ou égal à y.
Strictement parlant, les opérandes des opérateurs logiques doivent être des expressions booléennes, mais
Python n'est pas très strict. Tout nombre différent de zéro est interprété comme True:

5.4. Exécution conditionnelle

41

>>> 42 and True
True
Cette flexibilité peut être utile, mais certaines subtilités peuvent être déroutantes.
Vous voudrez peut-être l'éviter (sauf si vous savez ce que vous faites).

5.4

Exécution conditionnelle

Pour écrire des programmes utiles, nous avons presque toujours besoin de pouvoir vérifier les conditions
et modifier le comportement du programme en conséquence. Les déclarations conditionnelles nous donnent ceci
aptitude. La forme la plus simple est l'instruction if:

if x > 0:
print('x is positive')
L'expression booléenne après if s'appelle la condition. Si c'est vrai, la déclaration en retrait
s'exécute. Sinon, rien ne se passe.

les instructions if ont la même structure que les définitions de fonctions: un en-tête suivi d'un
corps en retrait. Des déclarations comme celles-ci sont appelées des déclarations composées.
Il n'y a pas de limite au nombre de déclarations pouvant apparaître dans le corps, mais il doit y avoir
au moins un. À l’occasion, il est utile d’avoir un corps sans déclaration (généralement
placekeeper pour le code que vous n'avez pas encore écrit). Dans ce cas, vous pouvez utiliser la déclaration de passage,
qui ne fait rien.

if x < 0:
pass

5.5

# TODO: besoin de gérer des valeurs négatives!

Exécution alternative

Une deuxième forme de l'instruction if est "exécution alternative", dans laquelle il existe deux possibilités et la condition détermine celle qui s'exécute. La syntaxe ressemble à ceci:

if x % 2 == 0:
print('x is even')
else:
print('x is odd')
Si le restant lorsque x est divisé par 2 est 0, alors nous savons que x est pair, et le programme
affiche un message approprié. Si la condition est fausse, la deuxième série de déclarations
s'exécute. Comme la condition doit être vraie ou fausse, l'une des alternatives s'exécutera exactement.
Les alternatives sont appelées branches, car elles sont des branches dans le flux d'exécution.

5.6

Chaînes conditionnels

Parfois, il y a plus de deux possibilités et nous avons besoin de plus de deux branches.
Une façon d'exprimer un calcul comme celui-là est un chaîne conditionnel:

42

Chapitre 5. Conditions et récursivité

if x < y:
print('x is less than y')
elif x > y:
print('x is greater than y')
else:
print('x and y are equal')
elif est une abréviation de "else if". Encore une fois, exactement une branche sera exécutée. Il n'y a pas de limite sur
le nombre de déclarations elif. S'il y a une clause else, elle doit être à la fin, mais
cela est facultatif.
if choice == 'a':
draw_a()
elif choice == 'b':
draw_b()
elif choice == 'c':
draw_c()
Chaque condition est vérifiée dans l'ordre. Si le premier est faux, le suivant est coché, et ainsi de suite. Si un
d'entre eux est vrai, la branche correspondante s'exécute et l'instruction se termine. Même si plus de
une condition est vraie, seule la première branche vraie s'exécute.

5.7

Conditionals imbriqués

Un conditionnel peut aussi être imbriqué dans un autre. Nous aurions pu écrire l'exemple dans
la section précédente comme ceci:

if x == y:
print('x and y are equal')
else:
if x < y:
print('x is less than y')
else:
print('x is greater than y')
Le conditionnel externe contient deux branches. La première branche contient une simple déclaration.
La seconde branche contient une autre instruction if, qui comporte deux branches.
Ces deux branches sont toutes deux des déclarations simples, bien qu’elles aient pu être 
conditionnelles.
Bien que l'indentation des déclarations rendent la structure apparente, les conditionnels imbriqués deviennent difficiles à lire très rapidement. C'est une bonne idée de les éviter quand vous
pouvez.
Les opérateurs logiques permettent souvent de simplifier les instructions conditionnelles imbriquées. Par exemple, nous pouvons réécrire le code suivant en utilisant un seul conditionnel:

if 0 < x:
if x < 10:
print('x is a positive single-digit number.')
L'instruction print ne s'exécute que si nous passons les deux conditions, afin que nous puissions obtenir la même chose
effet avec l'opérateur et:
if 0 < x and x < 10:
print('x is a positive single-digit number.')

5.8. Récursivité

43

Pour ce type de condition, Python fournit une option plus concise:

if 0 < x < 10:
print('x is a positive single-digit number.')

5.8

Récursivité

Il est légal qu'une fonction appelle une autre; il est également légal qu'une fonction s'appelle elle-même. Cela pourrait
ne pas être évident pourquoi c'est une bonne chose, mais il s'avère être l'un des choses les
plus magiques qu'un programme puisse faire. Par exemple, regardez la fonction suivante:

def countdown(n):
if n <= 0:
print('Blastoff!')
else:
print(n)
countdown(n-1)
Si n est 0 ou négatif, il affiche le mot "Blastoff!" Sinon, il affiche n puis appelle
une fonction nommée countdown (soi-même) en passant n-1 en argument.
Que se passe-t-il si nous appelons cette fonction comme ceci?

>>> countdown(3))
L’exécution du compte à rebours commence par n = 3, et comme n est supérieur à 0, il sort le
valeur 3, puis appelle lui-même ...
L’exécution du compte à rebours commence par n = 2, et comme n est supérieur à 0, il
génère la valeur 2 et appelle ensuite lui-même ...
L'exécution du compte à rebours commence par n = 1, et comme n est supérieur
à 0, il affiche la valeur 1, puis s'appelle lui-même ...
L'exécution du compte à rebours commence par n = 0, et comme n est
pas supérieur à 0, il affiche le mot "Blastoff!" et retorne
ensuite.
The countdown that got n=1 returns.
The countdown that got n=2 returns.
The countdown that got n=3 returns.
Et puis vous êtes de retour dans __main__. Ainsi, la sortie totale ressemble à ceci:
3
2
1
Blastoff!
Une fonction qui s'appelle elle-même est récursive; le processus d'exécution est appelé récursivité.
Comme autre exemple, nous pouvons écrire une fonction qui imprime une chaîne n fois.

def print_n(s, n):
if n <= 0:
return
print(s)
print_n(s, n-1)

44

Chapitre 5. Conditions et récursivité
__main__
countdown

n

3

countdown

n

2

countdown

n

1

countdown

n

0

Figure 5.1: Diagramme de pile.
Si n <= 0, l'instruction de retour quitte la fonction. Le flux d'exécution retourne immédiatement à l'appelant et les lignes restantes de la fonction ne s'exécutent pas.
Le reste de la fonction est similaire au compte à rebours: il affiche s puis appelle lui-même pour afficher
s n - 1 fois supplémentaires. Donc, le nombre de lignes de sortie est 1 + (n - 1), ce qui totalise
à n.
Pour des exemples simples comme celui-ci, il est probablement plus facile d'utiliser une boucle for. Mais on verra des
exemples plus tard qui sont difficiles à écrire avec une boucle for et facile à écrire avec la récursivité, de sorte qu'il
est bon de commencer tôt.

5.9

Diagrammes de pile pour les fonctions récursives

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

5.10

Récursion infinie

Si une récursivité n'atteint jamais un cas de base, elle continue à faire des appels récursifs pour toujours et le
programme ne se termine jamais. Ceci est connu comme la récursion infinie, et ce n'est généralement pas une
bonne idée. Voici un programme minimal avec une récursion infinie:

5.11. La saisie au clavier

45

def recurse ():
recurse ()
Dans la plupart des environnements de programmation, un programme avec une récursion infinie ne fonctionne pas vraiment
pour toujours. Python signale un message d'erreur lorsque la profondeur de récursivité maximale est atteinte:
maximum recursion depth is reached:
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
.
.
.
File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded
Cette traceback est un peu plus grande que celle que nous avons vue dans le chapitre précédent. Quand l'erreur
se produit, il y a 1000 cadres de recurse sur la pile!
Si vous rencontrez une récursion infinie par accident, révisez votre fonction pour confirmer que
il y a un cas de base qui ne fait pas un appel récursif. Et s'il y a un cas de base, vérifiez
si vous êtes assuré d'y accéder.

5.11

La saisie au clavier

Les programmes que nous avons écrits jusqu'à présent n'acceptent aucune contribution de l'utilisateur. Ils font juste la même chose
chose à chaque fois.
Python fournit une fonction intégrée appelée entrée qui arrête le programme et attend la
utilisateur de taper quelque chose. Lorsque l'utilisateur appuie sur Entrée ou Retour, le programme reprend et
input renvoie ce que l'utilisateur a tapé en tant que chaîne. Dans Python 2, la même fonction est appelée
raw_input.
>>> text = input()
What are you waiting for?
>>> text
'What are you waiting for?'
Avant d’obtenir les commentaires de l’utilisateur, il est conseillé d’imprimer une invite indiquant à l’utilisateur
taper input peut prendre une invite en argument:
>>> name = input('What...is your name?\n')
What...is your name?
Arthur, King of the Britons!
>>> name
'Arthur, King of the Britons!'
La séquence \ n à la fin de l'invite représente une nouvelle ligne, qui est un caractère spécial
cela provoque un saut de ligne. C'est pourquoi l'entrée de l'utilisateur apparaît sous l'invite.
Si vous vous attendez à ce que l'utilisateur tape un entier, vous pouvez essayer de convertir la valeur de retour en int:
>>> prompt = 'What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = input(prompt)
Qu'est-ce que la vitesse de vitesse d'une hirondelle à vide?
42
>>> int(speed)
42

46

Chapitre 5. Conditions et récursivité

Mais si l'utilisateur tape autre chose qu'une chaîne de chiffres, vous obtenez une erreur:
>>> speed = input(prompt)
Qu'est-ce que la vitesse de vitesse d'une hirondelle à vide?
Qu'est-ce que vous voulez dire, une hirondelle africaine ou européenne?
>>> int(speed)
ValueError: invalid literal for int() with base 10
Nous verrons comment gérer ce type d'erreur plus tard.

5.12

Le débogage

Lorsqu'une erreur de syntaxe ou d'exécution se produit, le message d'erreur contient beaucoup d'informations, mais
cela peut être accablant. Les parties les plus utiles sont généralement les suivantes:
• Quel type d'erreur était-ce et
• où il s'est produit.
Les erreurs de syntaxe sont généralement faciles à trouver, mais il y a quelques pièges. Les erreurs d'espacement peuvent
être difficile parce que les espaces et les onglets sont invisibles et nous sommes habitués à les ignorer.
>>> x = 5
>>> y = 6
File "<stdin>", line 1
y = 6
^
IndentationError: unexpected indent
Dans cet exemple, le problème est que la deuxième ligne est en retrait d'un espace. Mais l'erreur
le message indique y, ce qui est trompeur. En général, les messages d’erreur indiquent où
problème a été découvert, mais l'erreur réelle peut être antérieure dans le code, parfois sur un
ligne précédente
La même chose est vraie pour les erreurs d'exécution. Supposons que vous essayiez de calculer un rapport signal / bruit
ratio en décibels. La formule est SNRdb = 10 log10 ( Psignal /Pnoise ). En python, vous pourriez
écris quelque chose comme ceci:
import math
signal_power = 9
noise_power = 10
ratio = signal_power // noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
Lorsque vous exécutez ce programme, vous obtenez une exception:
Traceback (most recent call last):
File "snr.py", line 5, in ?
decibels = 10 * math.log10(ratio)
ValueError: math domain error
Le message d'erreur indique la ligne 5, mais il n'y a rien de mal avec cette ligne. Pour trouver le
erreur réelle, il pourrait être utile d’imprimer la valeur du ratio, qui se révèle être 0. Le
problème est à la ligne 4, qui utilise la division au sol au lieu de la division en virgule flottante.
Vous devriez prendre le temps de lire attentivement les messages d'erreur, mais ne présumez pas que tout
ils disent est correct.

5.13. Glossaire

5.13

47

Glossaire

Division de plancher / floor division: Un opérateur, noté //, qui divise deux nombres et arrondit à un entier inférieur (vers l'infini négatif).
opérateur de module / modulus operator: un opérateur, noté avec un signe de pourcentage (%), qui fonctionne sur des nombres entiers
et renvoie le reste lorsqu'un nombre est divisé par un autre.
expression booléenne: expression dont la valeur est True ou False.
opérateur relationnel: Un des opérateurs qui compare ses opérandes: ==,! =,>, <,> = et
<=.
opérateur logique: un des opérateurs combinant des expressions booléennes: et, ou
ne pas.
instruction conditionnelle: une instruction qui contrôle le flux d'exécution en fonction de certains
conditions.
condition: expression booléenne dans une instruction conditionnelle qui détermine une
branche court.
déclaration composée: déclaration composée d'un en-tête et d'un corps. L'en-tête se termine
avec deux points (:). Le corps est en retrait par rapport à l'en-tête.
branch: une des séquences alternatives d'instructions dans une instruction conditionnelle.
chained conditionnel: une instruction conditionnelle avec une série de branches alternatives.
conditionnel imbriqué: instruction conditionnelle qui apparaît dans l'une des branches d'une autre
déclaration conditionnelle.
instruction de retour: instruction qui entraîne la fin immédiate d'une fonction et le retour à la
votre interlocuteur.
récursivité: processus d'appel de la fonction en cours d'exécution.
cas de base: branche conditionnelle dans une fonction récursive qui ne fait pas un appel récursif.
récursion infinie: récursivité qui n'a pas de cas de base ou ne l'atteint jamais. Finalement, une récursion infinie provoque une erreur d'exécution.

5.14

Des exercices

Exercice 5.1. Le time fournit une fonction, également nommée time, qui renvoie le Greenwich Mean Time en tant "the epoch", qui est un temps arbitraire utilisé comme point de référence. Sur
Systèmes UNIX, epoch est le 1er janvier 1970.

>>> import time
>>> time.time()
1437746094.5735958
Écrivez un script qui lit l'heure actuelle et le convertit en heure, en minutes et en minutes.
secondes, plus le nombre de jours écoulés depuis l'époque.

48

Chapitre 5. Conditions et récursivité

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

def recurse(n, s):
if n == 0:
print(s)
else:
recurse(n-1, n+s)
recurse(3, 0)
1. Que se passerait-il si vous appeliez cette fonction comme ceci: recurse (-1, 0)?
2. Ecrivez un docstring qui explique tout ce que quelqu'un devrait savoir pour pouvoir l'utiliser
fonction (et rien d'autre).
Les exercices suivants utilisent le module tortue, décrit au chapitre 4:
Exercice 5.5. Lisez la fonction suivante et voyez si vous pouvez comprendre ce qu’elle fait (voir les exemples du chapitre 4). Puis lancez-le et voyez si vous avez bien compris.

5.14. Des exercices

49

Figure 5.2: Une courbe de Koch/ Koch curve.

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

50

Chapitre 5. Conditions et récursivitéChapitre 6

Fonctions fructueuses
Beaucoup de fonctions Python que nous avons utilisées, telles que les fonctions mathématiques, produisent des valeurs de
retour. Mais les fonctions que nous avons écrites sont toutes vides: elles ont un effet, comme imprimer un
valeur ou le déplacement d'une tortue, mais ils n'ont pas de valeur de retour. Dans ce chapitre, vous apprendrez à
écrire des fonctions fructueuses.

6.1

Valeurs de retour

L'appel de la fonction génère une valeur de retour, que nous l'affectons généralement à une variable ou à une utilisation.
dans le cadre d'une expression.

e = math.exp (1.0)
height = radius * math.sin (radians)
Les fonctions que nous avons écrites jusqu'à présent sont nulles. Parlant avec désinvolture, ils n'ont aucun valeur de
retour; plus précisément, leur valeur de retour est None.
Dans ce chapitre, nous allons (enfin) écrire des fonctions fructueuses. Le premier exemple est la zone,
qui renvoie l'aire d'un cercle du rayon donné:

def area(radius):
a = math.pi * radius**2
return a
Nous avons vu la déclaration de retour avant, mais dans une fonction fructueuse la déclaration de retour
comprend une expression. Cette déclaration signifie: "Retourner immédiatement de cette fonction
et utilisez l'expression suivante comme valeur de retour. "L'expression peut être arbitrairement
compliqué, nous aurions pu écrire cette fonction de manière plus concise:

def area(radius):
return math.pi * radius**2
En revanche, des variables temporaires telles que a peuvent faciliter le débogage.
Parfois, il est utile d'avoir plusieurs instructions de retour, une dans chaque branche d'un conditionnel:

52

Chapitre 6. Fonctions fructueuses

def absolute_value(x):
if x < 0:
return -x
else:
return x
Comme ces instructions de retour sont dans une autre condition, une seule est exécutée.
Dès qu'une instruction de retour s'exécute, la fonction se termine sans exécuter les instructions suivantes. Partie de code qui apparaît après une déclaration de retour, ou tout autre endroit que le flux
de l'exécution ne peut jamais atteindre, s'appelle le code mort.
Dans une fonction fructueuse, il est conseillé de s’assurer que chaque chemin possible du programme rencontre une déclaration de retour. Par exemple:

def absolute_value(x):
if x < 0:
return -x
if x > 0:
return x
Cette fonction est incorrecte car si x se trouve être 0, ni la condition est vraie, et le
fonction se termine sans frapper une déclaration de retour. Si le flux d'exécution arrive à la fin
d'une fonction, la valeur de retour est None, ce qui n'est pas la valeur absolue de 0.
>>> print(absolute_value(0))
None
Par ailleurs, Python fournit une fonction intégrée appelée abs qui calcule des valeurs absolues.
Comme exercice, écrire une fonction de comparaison prend deux valeurs, x et y, et renvoie 1 si x> y,
0 si x == y et -1 si x <y.

6.2

Développement incrémental

Au fur et à mesure que vous écrivez des fonctions plus grandes, vous risquez de devoir passer plus de temps à déboguer.
Pour gérer des programmes de plus en plus complexes, vous pouvez essayer un processus appelé développement incrémentiel. Le développement incrémentiel a pour but d'éviter le débogage de long
sessions en ajoutant et en testant seulement une petite quantité de code à la fois.
Par exemple, supposons que vous souhaitiez trouver la distance entre deux points, donnée par les
coordonnées (x1, y1) et (x2, y2). Par le théorème de Pythagore, la distance est:
distance =

q

(x2 - x1) 2 + (y2 - y1) 2

La première étape consiste à examiner à quoi devrait ressembler une fonction de distance en Python. En d'autre
mots, quelles sont les entrées (paramètres) et quelle est la sortie (valeur de retour)?
Dans ce cas, les entrées sont deux points que vous pouvez représenter en utilisant quatre chiffres. La
valeur de retour est la distance représentée par une valeur à virgule flottante.
Immédiatement, vous pouvez écrire un aperçu de la fonction:

def distance(x1, y1, x2, y2):
return 0.0

6.2. Développement incrémental

53

Evidemment, cette version ne calcule pas les distances; il retourne toujours zéro. Mais il est syntaxiquement correct et fonctionne, ce qui signifie que vous pouvez le tester avant de le rendre plus
compliqué.
Pour tester la nouvelle fonction, appelez-la avec des exemples d'arguments:
>>> distance(1, 2, 4, 6)
0.0
J'ai choisi ces valeurs pour que la distance horizontale soit de 3 et la distance verticale de 4; 
ainsi, le résultat est 5, l'hypoténuse d'un triangle 3-4-5. Lors du test d'une fonction, il est utile de
connaître la bonne réponse.
A ce stade, nous avons confirmé que la fonction est syntaxiquement correcte, et nous pouvons commencer
ajouter du code au corps. Une prochaine étape raisonnable consiste à trouver les différences x2 - x1 et
y2 - y1. La prochaine version stocke ces valeurs dans des variables temporaires et les imprime.
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
print('dx is', dx)
print('dy is', dy)
return 0.0
Si la fonction fonctionne, elle devrait afficher dx  3 et dy  4. Si oui, nous savons que le
la fonction consiste à obtenir les bons arguments et à effectuer le premier calcul correctement. Si
non, il n'y a que quelques lignes à vérifier.
Ensuite, nous calculons la somme des carrés de dx et dy:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
print('dsquared is: ', dsquared)
return 0.0
Encore une fois, vous devez exécuter le programme à ce stade et vérifier le résultat (qui doit être
25). Enfin, vous pouvez utiliser math.sqrt pour calculer et renvoyer le résultat:
def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
result = math.sqrt(dsquared)
return result
Si cela fonctionne correctement, vous avez terminé. Sinon, vous pouvez imprimer la valeur du
résultat avant la déclaration de retour.
La version finale de la fonction n'affiche rien quand elle s'exécute; il ne fait que retourner
une valeur. Les instructions d'impression que nous avons écrites sont utiles pour le débogage, mais une fois que vous obtenez le
fonction de travail, vous devez les supprimer. Les codes comme cela s'appellent échafaudage car ils
sont utiles pour construire le programme mais ne fait pas partie du produit final.
Lorsque vous commencez, vous ne devez ajouter qu'une ligne ou deux de code à la fois. Comme vous gagnez plus
d'expérience, vous pourriez vous retrouver à écrire et à déboguer de plus gros morceaux. D'une manière ou d'une autre,
le développement incrémentiel peut vous faire économiser beaucoup de temps de débogage.
Les aspects clés du processus sont les suivants:

54

Chapitre 6. Fonctions fructueuses
1. Commencez par un programme de travail et apportez de petites modifications incrémentielles. A tout moment, si
il y a une erreur, vous devriez avoir une bonne idée de la situation.
2. Utilisez des variables pour contenir des valeurs intermédiaires afin de pouvoir les afficher et les vérifier.
3. Une fois que le programme fonctionne, vous pouvez supprimer une partie de l’échafaudage ou
consolider plusieurs instructions dans des expressions composées, mais seulement si elles ne le font pas
rendre le programme difficile à lire.

Comme exercice, utilisez le développement incrémental pour écrire une fonction appelée hypoténuse qui
renvoie la longueur de l'hypoténuse d'un triangle rectangle étant donné la longueur des deux autres
jambes comme arguments. Enregistrez chaque étape du processus de développement au fur et à mesure.

6.3

Composition

Comme vous vous en doutez, vous pouvez appeler une fonction depuis une autre. Par exemple, nous allons écrire une fonction qui prend deux points, le centre du cercle et un point sur le
périmètre, et calcule l'aire du cercle.
Supposons que le point central est stocké dans les variables xc et yc et que le point de périmètre est
dans xp et yp. La première étape consiste à trouver le rayon du cercle, qui est la distance entre
les deux points. Nous venons écrire une fonction, distance, qui fait cela:

radius = distance(xc, yc, xp, yp)
L'étape suivante consiste à trouver l'aire d'un cercle avec ce rayon; nous venons d'écrire cela aussi:

result = area(radius)
En encapsulant ces étapes dans une fonction, nous obtenons:

def circle_area(xc, yc, xp, yp):
radius = distance(xc, yc, xp, yp)
result = area(radius)
return result
Les variables temporaires radius et result sont utiles pour le développement et le débogage,
mais une fois que le programme fonctionne, nous pouvons le rendre plus concis en composant les fonctions d'appels:

def circle_area(xc, yc, xp, yp):
return area(distance(xc, yc, xp, yp))

6.4

Fonctions booléennes

Les fonctions peuvent renvoyer des valeurs booléennes, ce qui est souvent pratique pour cacher des tests compliqués à l'intérieur de fonctions. Par exemple:

def is_divisible(x, y):
if x % y == 0:
return True
else:
return False

6.5. Plus de récursivité

55

Il est courant de donner des noms de fonctions booléens qui sonnent comme des questions oui / non;
is_divisible renvoie True ou False pour indiquer si x est divisible par y.
Voici un exemple:
>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True
Le résultat de l'opérateur == est un booléen, de sorte que nous pouvons écrire la fonction de manière plus concise en
le retournant directement:
def is_divisible(x, y):
return x % y == 0
Les fonctions booléennes sont souvent utilisées dans les instructions conditionnelles:
if is_divisible(x, y):
print('x is divisible by y')
Il pourrait être tentant d'écrire quelque chose comme:
if is_divisible(x, y) == True:
print('x is divisible by y')
Mais la comparaison supplémentaire est inutile.
En tant qu'exercice, écrivez une fonction is_between (x, y, z) qui renvoie True si x ≤ y ≤ z ou
Faux sinon.

6,5

Plus de récursivité

Nous avons seulement couvert un petit sous-ensemble de Python, mais vous pourriez être intéressé de savoir que
ce sous-ensemble est un langage de programmation complet, ce qui signifie que tout ce qui peut être
calculé peut être exprimé dans cette langue. Tout programme jamais écrit pourrait être réécrit
en utilisant uniquement les fonctionnalités de langue que vous avez apprises jusqu'à présent (en fait, vous auriez besoin de quelques
commandes pour contrôler les périphériques comme la souris, les disques, etc., mais c'est tout).
Prouver que cette affirmation n'est pas banale, voici un exercice accompli d’abord par Alan Turing, un des
premiers informaticiens (certains diront qu’il était mathématicien, mais beaucoup
d'informaticiens ont commencé comme mathématiciens). En conséquence, il est connu sous le nom du Thèse Turing. 
Pour une discussion plus complète (et précise) de la thèse de Turing, je vous recommande
le livre de Michael Sipser Introduction to the Theory of Computation.
Pour vous donner une idée de ce que vous pouvez faire avec les outils que vous avez appris jusqu'à présent, nous évaluerons quelques fonctions mathématiques définies récursivement. Une définition récursive est similaire à
une définition circulaire, en ce sens que la définition contient une référence à la chose
défini. Une définition vraiment circulaire n'est pas très utile:
vorpal: un adjectif utilisé pour décrire quelque chose qui est vorpal.
Si vous avez vu cette définition dans le dictionnaire, vous pourriez être ennuyé. D'autre part,
si vous avez regardé la définition de la fonction factorielle, notée avec le symbole!, vous
pourrait obtenir quelque chose comme ça:
0! = 1
n! = n (n - 1)!

56

Chapitre 6. Fonctions fructueuses

Cette définition dit que la factorielle de 0 est 1 et que la factorielle de toute autre valeur, n, est n
multiplié par la factorielle de n - 1.
Donc 3! est 3 fois 2 !, ce qui correspond à 2 fois 1 !, soit 1 fois 0 !. Tout rassembler, 3! est égal à 3
fois 2 fois 1 fois 1, soit 6.
Si vous pouvez écrire une définition récursive de quelque chose, vous pouvez écrire un programme Python sur
l'évaluez La première étape consiste à décider quels devraient être les paramètres. Dans ce cas, il devrait
être clair que factorial prend un entier:

def factorial(n):
Si l'argument arrive à 0, il suffit de retourner 1:

def factorial(n):
if n == 0:
return 1
Sinon, et ceci est la partie intéressante, nous devons faire un appel récursif pour trouver le
factorielle de n - 1 puis multiplie-la par n:

def factorial(n):
if n == 0:
return 1
else:
recurse = factorial(n-1)
result = n * recurse
return result
Le flux d'exécution de ce programme est similaire au flux de compte à rebours de la section 5.8. Si
nous appelons factorial avec la valeur 3:
Puisque 3 n'est pas 0, nous prenons la deuxième branche et calculons la factorielle de n-1 ...
Puisque 2 n'est pas 0, nous prenons la deuxième branche et calculons la factorielle de n-1 ...
Puisque 1 n'est pas 0, nous prenons la deuxième branche et calculons la factorielle
de n-1 ...
Puisque 0 est égal à 0, nous prenons la première branche et retournons 1 sans
faire plus d'appels récursifs.
La valeur de retour, 1, est multipliée par n, qui est 1, et le résultat est
revenu.
La valeur de retour, 1, est multipliée par n, qui est 2, et le résultat est renvoyé.
La valeur de retour (2) est multipliée par n, qui est 3, et le résultat 6 devient le retour
valeur de l'appel de fonction qui a démarré tout le processus.
La figure 6.1 montre à quoi ressemble le diagramme de la pile pour cette séquence d'appels de fonction.
Les valeurs de retour sont affichées lors de la remontée de la pile. Dans chaque cadre, le retour
valeur est la valeur du résultat, qui est le produit de n et recurse.
Dans la dernière exemple, les variables locales recurse et result n'existent pas, car la branche
qui les a crée ne fonctionne pas.

6.6. Acte de foi

57

__main__
6
factorial

n

3

recurse

2

result

6

factorial

n

2

recurse

1

result

2

factorial

n

1

recurse

1

result

1

factorial

n

0

2
1
1

Figure 6.1: Diagramme de pile.

6.6

Acte de foi

Suivre le flux d’exécution est une façon de lire les programmes, mais elle peut rapidement devenir
accablant. Une alternative est ce que j'appelle le "leap of faith". Quand vous arrivez à un
fonction appel, au lieu de suivre le flux d'exécution, vous supposez que la fonction fonctionne
correctement et renvoie le bon résultat.
En fait, vous pratiquez déjà cet acte de foi lorsque vous utilisez des fonctions intégrées. Quand
vous appelez math.cos ou math.exp, vous n'examinez pas les corps de ces fonctions. Nous
supposons qu'ils fonctionnent parce que les personnes qui ont écrit les fonctions intégrées étaient de bons
programmeurs.
La même chose est vraie lorsque vous appelez l'une de vos propres fonctions. Par exemple, dans la section 6.4, nous
avons écrit une fonction appelée is_divisible qui détermine si un nombre est divisible par
un autre. Une fois que nous nous sommes convaincus que cette fonction est correcte, en examinant le
code et test - nous pouvons utiliser la fonction sans regarder à nouveau le corps.
La même chose est vraie pour les programmes récursifs. Lorsque vous arrivez à l'appel récursif, au lieu de
suivre le flux d'exécution, vous devez supposer que l'appel récursif fonctionne (retourne
le résultat correct) et puis demandez-vous, "En supposant que je peux trouver la factorielle de n - 1,
puis-je calculer la factorielle de n? "Il est clair que vous pouvez, en multipliant par n.
Bien sûr, c'est un peu étrange de supposer que la fonction fonctionne correctement lorsque vous n'avez pas
fini de l'écrire, mais c'est pourquoi on appelle cela un acte de foi!

6,7

Un autre exemple

Après factorielle, l'exemple le plus commun d'une fonction mathématique définie récursivement est fibonacci, qui a la définition suivante (voir http://en.wikipedia.org/
wiki / Fibonacci_number):
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(n) = fibonacci(n − 1) + fibonacci(n − 2)
Traduit en Python, il ressemble à ceci:

58

Chapitre 6. Fonctions fructueuses

def fibonacci(n):
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n-1) + fibonacci(n-2)
Si vous essayez de suivre le flux d'exécution ici, même pour des valeurs assez petites de n, votre tête
explose. Mais selon le saut de foi, si vous supposez que les deux appels récursifs fonctionnent
correctement, il est clair que vous obtenez le bon résultat en les ajoutant ensemble.

6,8

Vérification des types

Que se passe-t-il si nous appelons factorial et lui donnons 1,5 comme argument?

>>> factorial(1.5)
RuntimeError: Maximum recursion depth exceeded
Cela ressemble à une récursion infinie. Comment ça peut survenir? La fonction a un cas de base lorsque n
== 0. Mais si n n'est pas un nombre entier, nous pouvons rater le cas de base et récurer pour toujours.
Dans le premier appel récursif, la valeur de n est 0,5. Dans le prochain, c'est -0.5. De là, ça devient
plus petit (plus négatif), mais il ne sera jamais 0.
Nous avons deux choix. Nous pouvons essayer de généraliser la fonction factorielle pour travailler avec
les nombres à virgule flottante, ou nous pouvons faire factoriel vérifier le type de son argument. le
La première option est appelée fonction gamma et dépasse un peu la portée de ce livre. Alors
nous irons pour le second.
Nous pouvons utiliser la fonction intégrée isinstance pour vérifier le type de l'argument. Tandis que
nous y sommes, nous pouvons également nous assurer que l'argument est positif:

def factorial(n):
if not isinstance(n, int):
print('Factorial is only defined for integers.')
return None
elif n < 0:
print('Factorial is not defined for negative integers.')
return None
elif n == 0:
return 1
else:
return n * factorial(n-1)
Le premier cas de base gère les non-entiers; le second traite les entiers négatifs. À la fois
Dans certains cas, le programme imprime un message d'erreur et renvoie None pour indiquer que quelque chose
s'est mal passé:
>>> print(factorial('fred'))
Factorial is only defined for integers.
None
>>> print(factorial(-2))
Factorial is not defined for negative integers.
None

6.9. Le débogage

59

Si nous passons les deux vérifications, nous savons que n est positif ou nul, nous pouvons donc prouver que le
la récursivité se termine.
Ce programme montre un modèle parfois appelé un tuteur. Les deux premières conditions agissent comme des gardiens, protégeant le code qui découle des valeurs susceptibles de provoquer
Erreur. Les gardiens permettent de prouver l'exactitude du code.
Dans la section 11.4, nous verrons une alternative plus flexible à l’impression d’un message d’erreur:
une exception.

6,9

Le débogage

Briser un grand programme en fonctions plus petites crée des points de contrôle naturels pour le débogage.
Si une fonction ne fonctionne pas, vous avez trois possibilités:
• Il y a quelque chose qui ne va pas dans les arguments obtenus par la fonction. une condition préalable
est violé.
• il y a quelque chose qui ne va pas dans la fonction; une post-condition est violée.
• Il y a un problème avec la valeur de retour ou la manière dont elle est utilisée.
Pour exclure la première possibilité, vous pouvez ajouter un relevé d'impression au début du
fonction et afficher les valeurs des paramètres (et peut-être leurs types). Ou vous pouvez
écrire le code qui vérifie explicitement les conditions préalables.
Si les paramètres sont corrects, ajoutez une instruction print avant chaque instruction de retour et
afficher la valeur de retour. Si possible, vérifiez le résultat à la main. Envisagez d'appeler la fonction
avec des valeurs facilitant la vérification du résultat (comme dans la section 6.2).
Si la fonction semble fonctionner, regardez l'appel de fonction pour vous assurer que la valeur de retour
est utilisé correctement (ou utilisé du tout!).
L'ajout d'instructions d'impression au début et à la fin d'une fonction peut aider à
exécution plus visible. Par exemple, voici une version de factorial avec des instructions d'impression:

def factorial(n):
space = ' ' * (4 * n)
print(space, 'factorial', n)
if n == 0:
print(space, 'returning 1')
return 1
else:
recurse = factorial(n-1)
result = n * recurse
print(space, 'returning', result)
return result
L'espace est une chaîne de caractères d'espace qui contrôle l'indentation de la sortie. Voici la
résultat de la factorielle (4):

60

Chapitre 6. Fonctions fructueuses

factorial 4
factorial 3
factorial 2
factorial 1
factorial 0
returning 1
returning 1
returning 2
returning 6
returning 24
Si vous ne comprenez pas le déroulement de l'exécution, ce type de résultat peut être utile. Ça prend
un peu de temps pour développer des échafaudages efficaces, mais un petit échafaudage peut économiser beaucoup de
débogage.

6.10

Glossaire

variable temporaire: variable utilisée pour stocker une valeur intermédiaire dans un calcul complexe.
code mort: partie d'un programme qui ne peut jamais s'exécuter, souvent parce qu'il apparaît après un déclaration de
retour.
développement incrémental: Un plan de développement de programme destiné à éviter le débogage par
ajouter et tester seulement une petite quantité de code à la fois.
échafaudage: code utilisé lors du développement du programme mais ne faisant pas partie de la finale
version.
guardian: Un modèle de programmation qui utilise une instruction conditionnelle pour rechercher et gérer des circonstances pouvant provoquer une erreur.

6.11

Des exercices

Exercice 6.1. Dessinez un diagramme de pile pour le programme suivant. Qu'est-ce que le programme imprime?

def b(z):
prod = a(z, z)
print(z, prod)
return prod
def a(x, y):
x = x + 1
return x * y
def c(x, y, z):
total = x + y + z
square = b(total)**2
return square

6.11. Des exercices

61

x = 1
y = x + 1
print(c(x, y+3, x+y))
Exercise 6.2. The Ackermann function, A(m, n), is defined:



n + 1
A(m, n) = A(m − 1, 1)


A(m − 1, A(m, n − 1))

if m = 0
if m > 0 and n = 0
if m > 0 and n > 0.

Voir http: // en. Wikipédia. Fonction org / wiki / Ackermann_. Ecrire une fonction nommée ack
qui évalue la fonction Ackermann. Utilisez votre fonction pour évaluer ack (3, 4), qui devrait être
125. Que se passe-t-il pour les plus grandes valeurs de m et n? Solution: http: // thinkpython2. com / code /
ackermann. py.
Exercice 6.3. Un palindrome est un mot qui est orthographié de la même façon, comme "noon"
et "redivider". Récursivement, un mot est un palindrome si les première et dernière lettres sont identiques et
le milieu est un palindrome.
Les fonctions suivantes prennent un argument de type chaîne et renvoient les lettres du premier, du dernier et du milieu:

def first(word):
return word[0]
def last(word):
return word[-1]
def middle(word):
return word[1:-1]
Nous verrons comment ils fonctionnent dans le chapitre 8.
1. Saisissez ces fonctions dans un fichier nommé palindrome.py et testez-les. Ce qui se passe si
vous appelez le milieu avec une chaîne avec deux lettres? Une lettre? Qu'en est-il de la chaîne vide,
qui est écrit '' et ne contient pas de lettres?
2. Écrivez une fonction appelée is_palindrome qui prend un argument de chaîne et renvoie True si elle
est un palindrome et faux autrement. Rappelez-vous que vous pouvez utiliser la fonction intégrée len
pour vérifier la longueur d'une chaîne.
Solution: http: // thinkpython2. com / code / palindrome_ soln. py.
Exercice 6.4. Un nombre, a, est une puissance de b s'il est divisible par b et a / b est une puissance de b. Écrire un
fonction appelée is_power qui prend les paramètres a et b et renvoie True si a est une puissance de b. Remarque:
vous devrez penser au cas de base.
Exercice 6.5. Le plus grand diviseur commun (GCD) de a et b est le plus grand nombre qui divise
les deux sans reste.
Une façon de trouver le GCD de deux nombres est basée sur l’observation que si r est le reste
a est divisé par b, alors gcd(a, b) = gcd (b, r). En tant que cas de base, nous pouvons utiliser gcd (a, 0) = a.
Ecrivez une fonction appelée gcd qui prend les paramètres a et b et retourne leur plus grand commun diviseur.
Crédit: Cet exercice est basé sur un exemple tiré de la structure et de l’interprétation des programmes informatiques d’Abelson et Sussman.

62

Chapitre 6. Fonctions fructueusesChapitre 7

Itération
Ce chapitre concerne l'itération, qui permet d'exécuter un bloc d'instructions à plusieurs reprises.
Nous avons vu une sorte d'itération, en utilisant la récursivité, dans la section 5.8. Nous avons aussi vu un autre type, en utilisant un
boucle for, dans la section 4.2. Dans ce chapitre, nous verrons un autre type, en utilisant une instruction while.
Mais je veux d'abord en dire un peu plus sur l'affectation de variables.

7.1

Réaffectation

Comme vous avez pu le constater, il est légal de confier plusieurs affectations à la même
variable. Une nouvelle affectation fait qu'une variable existante se réfère à une nouvelle valeur (et arrête
de faire référence à l'ancienne valeur).

>>>
>>>
5
>>>
>>>
7

x = 5
X
x = 7
X

La première fois que nous affichons x, sa valeur est 5; la deuxième fois, sa valeur est 7.
Le dessin 7.1 montre à quoi ressemble la réaffectation dans un diagramme d'état.
À ce stade, je veux aborder une source commune de confusion. Parce que Python utilise le
signe égal (=) pour l'affectation, il est tentant d'interpréter un énoncé comme a = b comme une proposition mathématique d'égalité; c'est-à-dire que a et b sont égaux. Mais cette interprétation est fausse.
Tout d'abord, l'égalité est une relation symétrique et l'affectation ne l'est pas. Par exemple, en mathématiques, si a = 7 alors 7 = a. Mais en Python, l'instruction a = 7 est légale de 7 = a
est faux.
De plus, en mathématiques, une proposition d’égalité est vraie ou faux pour tous les temps. Si a =
b maintenant, alors b sera toujours égal à a. En Python, une instruction d'affectation peut faire deux
variables égales, mais ils ne doivent pas rester comme ça:

64

Chapitre 7. Itération

X

5
7

Figure 7.1: Diagramme d'état.

>>>
>>>
>>>
>>>
5

a = 5
b = a
a = 3
b

# a et b sont maintenant égaux
# a et b ne sont plus égaux

La troisième ligne change la valeur de a mais ne change pas la valeur de b, donc elles ne sont pas
plus égal
La réaffectation des variables est souvent utile, mais vous devez l'utiliser avec prudence. Si les valeurs des
variables changent fréquemment, cela peut rendre le code difficile à lire et à déboguer.

7.2

Mise à jour des variables

Un type courant de réaffectation est une mise à jour, où la nouvelle valeur de la variable dépend
sur l'ancien

>>> x = x + 1
Cela signifie "obtenir la valeur actuelle de x, ajouter un, puis mettre à jour x avec la nouvelle valeur."
Si vous essayez de mettre à jour une variable qui n’existe pas, vous obtenez une erreur, car Python évalue
le côté droit avant d'assigner une valeur à x:

>>> x = x + 1
NameError: name 'x' is not defined
Avant de pouvoir mettre à jour une variable, vous devez l'initialiser, généralement avec une affectation simple:

>>> x = 0
>>> x = x + 1
La mise à jour d'une variable en ajoutant 1 est appelée un incrément; soustraire 1 est appelé décrément.

7.3

La boucle while

Les ordinateurs sont souvent utilisés pour automatiser des tâches répétitives. Répéter des tâches identiques ou similaires
sans faire d'erreurs est quelque chose que les ordinateurs font bien et que les gens font mal. Dans un
programme informatique, la répétition est aussi appelée itération.
Nous avons déjà vu deux fonctions, countdown et print_n, qui itèrent en utilisant la récursivité.
Comme l'itération est si courante, Python fournit des fonctionnalités de langage pour le rendre plus facile. Un
est la déclaration for que nous avons vue à la section 4.2. Nous y reviendrons plus tard.
Une autre est la boucle while. Voici une version du compte à rebours qui utilise une instruction while:

7.3. La boucle while

65

def countdown(n):
while n > 0:
print(n)
n = n - 1
print('Blastoff!')
Vous pouvez presque lire la déclaration while comme si c'était l'anglais. Cela signifie que "Alors que n est plus grand
que 0, affiche la valeur de n puis décrémente n. Lorsque vous arrivez à 0, affichez le mot
blastoff"
Plus formellement, voici le déroulement de l’exécution:
1. Déterminez si la condition est vraie ou fausse.
2. Si la valeur est false, quittez l'instruction while et continuez l'exécution à l'instruction suivante.
3. Si la condition est vraie, lancez le corps et retournez à l'étape 1.
Ce type de flux est appelé une boucle car la troisième étape est bouclée vers le haut.
Le corps de la boucle devrait changer la valeur d'une ou plusieurs variables pour que la condition
devient finalement faux et la boucle se termine. Sinon, la boucle se répètera pour toujours,
qui s'appelle une boucle infinie. Une source d'amusement sans fin pour les informaticiens
est l'observation que les instructions sur le shampooing, "Lather, rinse, repeat", est une boucle
infinie.
Dans le cas du compte à rebours, on peut prouver que la boucle se termine: si n est zéro ou négatif, le
boucle ne fonctionne jamais. Sinon, n diminue chaque fois à travers la boucle, donc finalement nous
doivent arriver à 0.
Pour d'autres boucles, ce n'est pas si facile à dire. Par exemple:

def sequence(n):
while n != 1:
print(n)
if n % 2 == 0:
# n is even
n = n / 2
else:
# n is odd
n = n*3 + 1
La condition pour cette boucle est n! = 1, donc la boucle continuera jusqu'à ce que n soit 1, ce qui rend
la condition fausse.
À chaque fois dans la boucle, le programme affiche la valeur de n et vérifie ensuite si
c'est pair ou impair. Si c'est pair, n est divisé par 2. S'il est impair, la valeur de n est remplacée par
n * 3 + 1. Par exemple, si l'argument passé à la séquence est 3, les valeurs résultantes de n
sont 3, 10, 5, 16, 8, 4, 2, 1.
Comme n augmente et diminue parfois, il n’ya pas de preuve évidente que n
atteindra 1, ou que le programme se termine. Pour certaines valeurs particulières de n, nous pouvons prouver
la términaison. Par exemple, si la valeur de départ est une puissance de deux, n sera pair à
chaque fois dans la boucle jusqu'à ce qu'il atteigne 1. L'exemple précédent se termine par une telle séquence,
à partir de 16.
La question difficile est de savoir si nous pouvons prouver que ce programme se termine pour toutes les valeurs positives de n. Jusqu'à présent, personne n'a été capable de le prouver ou de le réfuter! (Voir http:
//en.wikipedia.org/wiki/Collatz_conjecture.)

66

Chapitre 7. Itération

En guise d’exercice, réécrivez la fonction print_n de la section 5.8 en utilisant l’itération au lieu de
récursivité.

7,4

Pause

Parfois, vous ne savez pas qu'il est temps de terminer une boucle jusqu'à ce que vous atteigniez la moitié du corps.
Dans ce cas, vous pouvez utiliser l'instruction break pour sortir de la boucle.
Par exemple, supposons que vous souhaitiez saisir les informations de l'utilisateur jusqu'à ce qu'elles soient saisies. Vous pourriez
écrire:
while True:
line = input('> ')
if line == 'done':
break
print(line)

print('Done!')
La condition de la boucle est True, ce qui est toujours vrai, donc la boucle s'exécute jusqu'à ce qu'elle atteigne la déclaration de
rupture.
À chaque fois, l'utilisateur est invité à choisir une option. Si l'utilisateur type 'done' (terminé), l'
instruction break quitte la boucle. Sinon, le programme reimprime ce que l'utilisateur type et
retourne au sommet de la boucle. Voici un exemple:
> not done
not done
> done
Done!
Cette façon d'écrire des boucles est commune car vous pouvez vérifier la condition n'importe où
dans la boucle (pas seulement en haut) et vous pouvez exprimer la condition d'arrêt de manière affirmative ("arretez
quand cela se produit ") plutôt que négativement (" continuez jusqu'à ce que cela arrive ").

7.5

Racines carrées

Les boucles sont souvent utilisées dans les programmes qui calculent des résultats numériques en commençant par une réponse approximative et en l'améliorant de manière itérative.
Par exemple, une méthode de calcul des racines carrées est la méthode de Newton. Supposons que vous
voulez savoir la racine carrée de a. Si vous commencez avec presque n'importe quelle estimation, x, vous pouvez calculer une meilleure estimation avec la formule suivante:
y =
Par exemple, si a est 4 et que x est 3:
>>> a = 4
>>> x = 3
>>> y = (x + a / x) / 2
>>> y
2.16666666667

x + a / x
2

7.6. Algorithmes

67

√
Le résultat est plus proche de la réponse correcte (4 = 2). Si nous répétons le processus avec le nouveau
estimation, il devient encore plus proche:
>>> x = y
>>> y = (x + a / x) / 2
>>> y
2.00641025641
Après quelques mises à jour supplémentaires, l'estimation est presque exacte:
>>> x = y
>>> y = (x + a / x) / 2
>>> y
2.00001024003
>>> x = y
>>> y = (x + a / x) / 2
>>> y
2.00000000003
En général, nous ne savons pas combien de temps il faut pour arriver à la bonne réponse,
mais on sait quand on arrive là-bas car le devis cesse de changer:
>>> x = y
>>> y = (x + a / x) / 2
>>> y
2.0
>>> x = y
>>> y = (x + a / x) / 2
>>> y
2.0
Lorsque y == x, on peut s'arrêter. Voici une boucle qui commence par une estimation initiale, x, et l'améliore jusqu'à ce qu'elle cesse de changer:
alors que vrai:
while True:
print(x)
y = (x + a/x) / 2
if y == x:
break
x = y
Pour la plupart des valeurs de a, cela fonctionne bien, mais en général, il est dangereux de tester l'égalité des flottants.
Les valeurs à virgule flottante sont approximativement correctes: la plupart des nombres rationnels, comme 1/3, et
les nombres irrationnels, comme 2, ne peuvent pas être représentés exactement avec un flottant.
Plutôt que de vérifier si x et y sont exactement égaux, il est préférable d'utiliser la fonction intégrée abs pour calculer la valeur absolue, ou l'ampleur, de la différence entre eux:

if abs(y-x) < epsilon:
break
Où epsilon a une valeur comme 0.0000001 qui détermine la proximité est assez proche.

7.6

Algorithmes

La méthode de Newton est un exemple d'algorithme: c'est un processus mécanique pour résoudre un
catégorie de problèmes (dans ce cas, calcul des racines carrées).

68

Chapitre 7. Itération

Pour comprendre ce qu'est un algorithme, il peut être utile de commencer par quelque chose qui n'est pas un
algorithme. Lorsque vous avez appris à multiplier des nombres à un chiffre, vous avez probablement mémorisé
la table de multiplication. En effet, vous avez mémorisé 100 solutions spécifiques. Ce genre de
connaissance n'est pas algorithmique.
Mais si vous étiez "paresseux", vous avez peut-être appris quelques astuces. Par exemple, pour trouver le
produit de n et 9, vous pouvez écrire n-1 comme premier chiffre et 10-n comme deuxième chiffre.
Cette astuce est une solution générale pour multiplier un nombre à un chiffre par 9. C'est un
algorithme!
De même, les techniques que vous avez apprises pour l'addition avec transport, la soustraction avec emprunt et la division longue sont toutes des algorithmes. L'une des caractéristiques des algorithmes est que
ils n'ont besoin d'aucune intelligence pour effectuer. Ce sont des processus mécaniques où
chaque étape découle de la dernière selon un ensemble simple de règles.
L'exécution d'algorithmes est ennuyeuse, mais leur conception est intéressante, un défi intellectuel et constitue un élément central de l'informatique.
Certaines des choses que les gens font naturellement, sans difficulté, ni pensée consciente, sont:
le plus difficile à exprimer algorithmiquement. Comprendre le langage naturel est un bon exemple.
Nous le faisons tous, mais jusqu’à présent, personne n’a pu expliquer comment nous le faisons, du moins pas sous la forme
d'un algorithme.

7.7

Le débogage

Lorsque vous commencez à écrire de plus gros programmes, vous risquez de devoir passer plus de temps à déboguer. Plus de code signifie plus de chances de faire une erreur et plus d'endroits où les bogues peuvent se cacher.
Un moyen de réduire votre temps de débogage est le "débogage par bissection". Par exemple, s'il y a
sont 100 lignes dans votre programme et vous les vérifiez un par un, cela prendrait 100 étapes.
Au lieu de cela, essayez de briser le problème en deux. Regardez au milieu du programme, ou à proximité, pour
une valeur intermédiaire que vous pouvez vérifier. Ajouter un relevé d'impression (ou autre chose qui a un
effet vérifiable) et exécuter le programme.
Si la vérification à mi-parcours est incorrecte, il doit y avoir un problème dans la première moitié du programme.
Si c'est correct, le problème est dans la seconde moitié.
Chaque fois que vous effectuez une vérification comme celle-ci, vous divisez par deux le nombre de lignes à rechercher.
Après six étapes (moins de 100), vous seriez réduit à une ou deux lignes de code,
au moins en théorie.
En pratique, il n'est pas toujours évident de savoir ce que le "milieu du programme" est et n'est pas toujours possible de vérifier. Cela n'a aucun sens de compter les lignes et de trouver le point médian exact. Au lieu,
penser à des endroits du programme où il peut y avoir des erreurs et des endroits faciles à
mettre un checkpoint. Ensuite, choisissez un endroit où vous pensez que les chances sont à peu près les mêmes
le bug est avant ou après la vérification.

7.8

Glossaire

réaffectation: attribuer une nouvelle valeur à une variable qui existe déjà.

7.9. Des exercices

69

update: Affectation où la nouvelle valeur de la variable dépend de l'ancienne.
initialization: une affectation qui donne une valeur initiale à une variable qui sera mise à jour.
increment: une mise à jour qui augmente la valeur d'une variable (souvent par une seule).
décrément: une mise à jour qui diminue la valeur d'une variable.
iteration: exécution répétée d'un ensemble d'instructions à l'aide d'un appel de fonction récursif
ou une boucle.
boucle infinie: boucle dans laquelle la condition de terminaison n'est jamais satisfaite.
algorithme: un processus général pour résoudre une catégorie de problèmes.

7,9

Des exercices

Exercice 7.1. Copiez la boucle de la section 7.5 et encapsulez-la dans une fonction appelée mysqrt
prend un comme paramètre, choisit une valeur raisonnable de x et renvoie une estimation de la racine carrée de
une.
Pour le tester, écrivez une fonction nommée test_square_root qui imprime un tableau comme celui-ci:

a
mysqrt (a)
math.sqrt (a) diff
-------------------- --- 1.0 1.0
1.0
0.0
2,0 1,41421356237 1,41421356237 2,22044604925e-16
3,0 1,73205080757 1,73205080757 0,0
4.0 2.0
2.0
0.0
5,0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0
3.0
0.0
La première colonne est un nombre, a; la deuxième colonne est la racine carrée d'un calcul avec mysqrt;
la troisième colonne est la racine carrée calculée par math.sqrt; la quatrième colonne est la valeur absolue
de la différence entre les deux estimations.
Exercice 7.2. La fonction intégrée eval prend une chaîne et l'évalue à l'aide de l'interpréteur Python. Par exemple:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Ecrire une fonction appelée eval_loop qui invite de manière itérative l'utilisateur, prend l'entrée résultante et
l'évalue en utilisant eval et imprime le résultat.
Il doit continuer jusqu'à ce que l'utilisateur entre "done", puis renvoyer la valeur de la dernière expression
évalué.

70

Chapitre 7. Itération

Exercice 7.3. Le mathématicien Srinivasa Ramanujan a trouvé une série infinie qui peut être utilisée pour
générer une approximation numérique de 1 / π:

√
2 2 ∞ (4k)!(1103 + 26390k )
1
=
π
9801 k∑
(k!)4 3964k
=0
Ecrivez une fonction appelée estimation_pi qui utilise cette formule pour calculer et renvoyer une estimation de
π. Il devrait utiliser une boucle while pour calculer les termes de la sommation jusqu'à ce que le dernier terme soit plus petit que
1e-15 (qui est la notation Python pour 10-15). Vous pouvez vérifier le résultat en le comparant à math.pi.
Solution: http: // thinkpython2. com / code / pi. py.Chapitre 8

Strings
Les chaînes ne sont pas des entiers, des flottants et des booléens. Une chaîne est une séquence, ce qui signifie qu'elle est
une collection ordonnée d'autres valeurs. Dans ce chapitre, vous verrez comment accéder aux caractères
qui constituent une chaîne, et vous apprendrez certaines des méthodes fournies par les chaînes.

8.1

Une chaîne est une séquence

Une chaîne est une séquence de caractères. Vous pouvez accéder aux personnages un par un avec le
opérateur de support:

>>> fruit = 'banana'
>>> letter = fruit[1]
La deuxième instruction sélectionne le numéro 1 du fruit et l'affecte à la lettre.
L'expression entre parenthèses s'appelle un index. L'index indique quel caractère dans le
séquence que vous voulez (d'où le nom).
Mais vous pourriez ne pas avoir ce que vous attendez:

>>> letter
'a'
Pour la plupart des gens, la première lettre de «banane» est b, pas a. Mais pour les informaticiens, le
index est un décalage par rapport au début de la chaîne et le décalage de la première lettre est zéro.
>>> letter = fruit[0]
>>> letter
'b'
Donc b est la 0ème lettre ("zero-eth") de "banane", a est la 1ère lettre ("one-eth"), et n est le 2eme
lettre ("two-eth").
En tant qu’index, vous pouvez utiliser une expression contenant des variables et des opérateurs:

>>> i = 1
>>> fruit[i]
'a'
>>> fruit[i+1]
'n'

72

Chapitre 8. Chaînes

Mais la valeur de l'index doit être un entier. Sinon, vous obtenez:

>>> letter = fruit[1.5]
TypeError: string indices must be integers

8.2

len

len est une fonction intégrée qui renvoie le nombre de caractères d'une chaîne:
>>> fruit = 'banana'
>>> len(fruit)
6
Pour obtenir la dernière lettre d'une chaîne, vous pourriez être tenté d'essayer quelque chose comme ceci:

>>> length = len(fruit)
>>> last = fruit[length]
IndexError: string index out of range
La raison de l’indexError est qu’il n’ya pas de lettre dans «banana» avec l’index 6.
nous avons commencé à compter à zéro, les six lettres sont numérotées de 0 à 5. Pour obtenir le dernier caractère,
vous devez soustraire 1 de la longueur:

>>> last = fruit[length-1]
>>> last
'a'
Ou vous pouvez utiliser des index négatifs, qui comptent à partir de la fin de la chaîne. le
expression fruit [-1] donne la dernière lettre, fruit [-2] renvoie la seconde à la dernière, et ainsi de suite.

8.3

Traversal avec une boucle for

De nombreux calculs impliquent le traitement d'une chaîne par caractère. Ils commencent souvent
au début, sélectionnez chaque personnage à son tour, faites-lui quelque chose et continuez jusqu'à la
fin. Ce modèle de traitement s'appelle une traversée. Une façon d'écrire une traversée est d'utiliser un
un boucle:

index = 0
while index < len(fruit):
letter = fruit[index]
print(letter)
index = index + 1
Cette boucle traverse la chaîne et affiche chaque lettre sur une ligne. La condition de la boucle
est index < len(fruit), donc quand index est égal à la longueur de la chaîne, la condition est
false et le corps de la boucle ne s'exécute pas. Le dernier personnage accédé est celui avec le
index len (fruit) -1, qui est le dernier caractère de la chaîne.
En tant qu’exercice, écrivez une fonction qui prend une chaîne comme argument et affiche les lettres
en arrière, un par ligne.
Une autre façon d'écrire une traversée consiste à utiliser une boucle for:

for letter in fruit:
print(letter)

8.4. Tranches de chaîne

73
fruit

’ banana’

index 0

1

2

3

4

5

6

Figure 8.1: Indices de tranches.
A chaque fois dans la boucle, le caractère suivant de la chaîne est assigné à la variable
lettre. La boucle continue jusqu'à ce qu'il ne reste plus aucun caractère.
L'exemple suivant montre comment utiliser la concaténation (ajout de chaîne) et une boucle for
pour générer une série abécédaire (c'est-à-dire par ordre alphabétique). Dans le livre de Robert McCloskey's
Make Way for Ducklings, les noms des canetons sont Jack, Kack, Lack, Mack, Nack,
Ouack, Pack et Quack. Cette boucle génère ces noms dans l'ordre:

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
print(letter + suffix)
The output is:

Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack
Bien sûr, ce n'est pas tout à fait correct, car "Ouack" et "Quack" sont mal orthographiés. En tant qu'exercice, 
modifiez le programme pour corriger cette erreur.

8.4

Tranches de chaîne

Un segment d'une chaîne est appelé une tranche. La sélection d'une tranche est similaire à la sélection d'un caractère:

>>> s = 'Monty Python'
>>> s [0: 5]
'Monty'
>>> s [6:12]
'Python'
L'opérateur [n: m] renvoie la partie de la chaîne du caractère "n-eth" au "m-eth"
, y compris le premier mais excluant le dernier. Ce comportement est contre-intuitif, mais
il pourrait être utile d'imaginer les indices pointant entre les caractères, comme dans la figure 8.1.
Si vous omettez le premier index (avant les deux points), la tranche commence au début de la chaîne.
Si vous omettez le deuxième index, la tranche va à la fin de la chaîne:

>>> fruit = 'banana'
>>> fruit[:3]

74

Chapitre 8. Chaînes

'ban'
>>> fruit[3:]
'ana'
Si le premier index est supérieur ou égal au second, le résultat est une chaîne vide, représentée par deux guillemets:

>>> fruit = 'banana'
>>> fruit[3:3]
''
Une chaîne vide ne contient aucun caractère et a la longueur 0, mais à part ça, c'est la même chose
comme toute autre chaîne.
Poursuivant cet exemple, à votre avis, que veut dire fruit [:]? Essayez-le et voyez.

8.5

Les caractères sont immuables

Il est tentant d’utiliser l’opérateur [] à gauche d’une affectation, avec l’intention de
changer un caractère dans une chaîne. Par exemple:

>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
Le "objet" dans ce cas est la chaîne et "l'élément" est le caractère que vous avez essayé d'attribuer.
Pour l'instant, un objet est la même chose qu'une valeur, mais nous affinerons cette définition ultérieurement
(Section 10.10).
La raison de l'erreur est que les chaînes sont immuables, ce qui signifie que vous ne pouvez pas changer un
chaîne existante. Le mieux que vous puissiez faire est de créer une nouvelle chaîne qui est une variante de l'original:

>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> new_greeting
'Jello, world!'
Cet exemple concatène une nouvelle première lettre sur une tranche de message d'accueil. Cela n'a aucun effet sur le
chaîne originale.

8.6

Recherche

Que fait la fonction suivante?

def find(word, letter):
index = 0
while index < len(word):
if word[index] == letter:
return index
index = index + 1
return -1

8.7. En boucle et compter

75

En un sens, find est l'inverse de l'opérateur []. Au lieu de prendre un index et d’extraire
le caractère correspondant, il prend un caractère et trouve l'index où ce caractère
apparaît. Si le caractère n'est pas trouvé, la fonction renvoie -1.
C'est le premier exemple que nous avons vu d'une déclaration de retour dans une boucle. Si mot [index]
== lettre, la fonction sort de la boucle et revient immédiatement.
Si le caractère n'apparaît pas dans la chaîne, le programme quitte la boucle normalement et renvoie -1.
Ce modèle de calcul-traversant une séquence et retournant quand on trouve ce que l'on
sont à la recherche-est appelé une recherche.
En tant qu’exercice, modifiez la recherche pour qu’elle ait un troisième paramètre, l’index dans le mot où
devrait commencer à regarder.

8.7

En boucle et compter

Le programme suivant compte le nombre de fois que la lettre a apparaît dans une chaîne:

word = 'banana'
count = 0
for letter in word:
if letter == 'a':
count = count + 1
print(count)
Ce programme montre un autre modèle de calcul appelé compteur. La variable
count est initialisé à 0 puis incrémenté chaque fois qu'un a est trouvé. Lorsque la boucle se termine,
count contient le résultat - le nombre total de a.
En guise d’exercice, encapsulez ce code dans une fonction nommée count et généralisez-le pour que
il accepte la chaîne et la lettre comme arguments.
Ensuite, réécrivez la fonction de sorte que, au lieu de parcourir la chaîne, elle utilise la version à trois paramètres de find de la section précédente.

8,8

Méthodes de chaîne

Les chaînes fournissent des méthodes permettant d'effectuer diverses opérations utiles. Une méthode est similaire
à une fonction, elle prend des arguments et retourne une valeur, mais la syntaxe est différente. Pour
Par exemple, la méthode upper prend une chaîne et retourne une nouvelle chaîne avec toutes les majuscules
des lettres.
Au lieu de la syntaxe de fonction supérieure (mot), elle utilise la syntaxe de la méthode word.upper ().

>>> word = 'banana'
>>> new_word = word.upper()
>>> new_word
'BANANA'

76

Chapitre 8. Chaînes

Cette forme de notation par points spécifie le nom de la méthode, supérieure et le nom de la
chaîne pour appliquer la méthode à, mot. Les parenthèses vides indiquent que cette méthode
ne prend aucun argument.
Un appel de méthode est appelé une invocation; dans ce cas, nous dirions que nous invoquons
supérieur sur le mot.
Comme il se trouve, il existe une méthode de chaîne nommée find qui est remarquablement similaire à la
fonction nous avons écrit:

>>> word = 'banana'
>>> index = word.find('a')
>>> index
1
Dans cet exemple, nous invoquons find sur word et transmettons la lettre que nous recherchons en tant que paramètre.
En fait, la méthode de recherche est plus générale que notre fonction; il peut trouver des sous-chaînes, pas seulement
personnages:

>>> word.find ('na')
2
Par défaut, find commence au début de la chaîne, mais il peut prendre un deuxième argument, le
index où il devrait commencer:

>>> word.find ('na', 3)
4
Ceci est un exemple d'un argument optionnel; find peut aussi prendre un troisième argument, l'index
où il devrait s'arrêter:

>>> name = 'bob'
>>> name.find ('b', 1, 2)
-1
Cette recherche échoue car b n'apparaît pas dans la plage d'index de 1 à 2, sans inclure 2.
Recherche jusqu'au, mais non compris, le deuxième index rend la recherche cohérente avec l'opérateur de
tranche.

8,9

L'opérateur in

Le mot in est un opérateur booléen qui prend deux chaînes et renvoie True si le premier apparaît comme une sous-chaîne dans le second:

>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
Par exemple, la fonction suivante imprime toutes les lettres de word1 qui apparaissent également dans
mot2:

def in_both(word1, word2):
for letter in word1:
if letter in word2:
print(letter)

8.10. Comparaison de chaîne

77

Avec des noms de variables bien choisis, Python se lit parfois comme l'anglais. Vous pouvez lire
cette boucle, "pour (chaque) lettre dans (le premier) mot, si (la) lettre (apparaît) dans (le second) mot,
imprimer la lettre. "
Voici ce que vous obtenez si vous comparez des pommes et des oranges:

>>> in_both('apples', 'oranges')
a
e
s

8.10

Comparaison de chaîne

Les opérateurs relationnels travaillent sur des chaînes. Pour voir si deux chaînes sont égales:

if word == 'banana':
print('All right, bananas.')
D'autres opérations relationnelles sont utiles pour mettre les mots en ordre alphabétique:

if word < 'banana':
print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
print('Your word, ' + word + ', comes after banana.')
else:
print('All right, bananas.')
Python ne gère pas les lettres majuscules et minuscules de la même manière que les gens. Tous les
les lettres majuscules viennent avant toutes les lettres minuscules, donc:

Votre mot, ananas, vient avant la banane.
Une méthode courante pour résoudre ce problème consiste à convertir des chaînes en un format standard, tel que
tout en minuscule, avant d'effectuer la comparaison. Gardez cela à l'esprit au cas où vous devriez
Défendez-vous contre un homme armé d'un Ananas.

8.11

Le débogage

Lorsque vous utilisez des indices pour parcourir les valeurs dans une séquence, il est difficile de commencer
et fin du parcours à droite. Voici une fonction censée comparer deux mots
et retourner True si l'un des mots est l'inverse de l'autre, mais il contient deux erreurs:

def is_reverse(word1, word2):
if len(word1) != len(word2):
return False
i = 0
j = len(word2)
while j > 0:
if word1[i] != word2[j]:
return False
i = i+1

78

Chapitre 8. Chaînes

j = j-1
return True
La première instruction if vérifie si les mots ont la même longueur. Sinon, nous pouvons retourner
False immédiatement Sinon, pour le reste de la fonction, on peut supposer que les mots
sont la même longueur Ceci est un exemple du modèle de gardien dans la section 6.8.
i et j sont des indices: i traverse mot1 en avant tandis que j traverse mot2 en arrière. Si nous
trouver deux lettres qui ne correspondent pas, nous pouvons retourner False immédiatement. Si nous passons à travers le
boucle entière et toutes les lettres correspondent, nous retournons True.
Si nous testons cette fonction avec les mots "pots" et "stop", nous attendons la valeur de retour True,
mais nous obtenons un IndexError:
>>> is_reverse('pots', 'stop')
...
File "reverse.py", line 15, in is_reverse
if word1[i] != word2[j]:
IndexError: string index out of range
Pour déboguer ce genre d'erreur, je commence par imprimer les valeurs des indices immédiatement avant la ligne où l'erreur apparaît.
while j > 0:
print(i, j)
# print here

if word1[i] != word2[j]:
return False
i = i+1
j = j-1
Maintenant, lorsque je relance le programme, je reçois plus d'informations:
>>> is_reverse ('pots', 'stop')
0 4
...
IndexError: index de chaîne hors limites
La première fois dans la boucle, la valeur de j est 4, ce qui est hors de portée pour le
chaîne 'pots'. L'index du dernier caractère est 3, donc la valeur initiale de j devrait être
len (word2) -1.
Si je corrige cette erreur et lance à nouveau le programme, j'obtiens:
>>> is_reverse ('pots', 'stop')
0 3
1 2
2 1
True
Cette fois, nous obtenons la bonne réponse, mais il semble que la boucle ne soit exécutée que trois fois, ce qui est
méfiant. Pour avoir une meilleure idée de ce qui se passe, il est utile de dessiner un diagramme d'état.
Au cours de la première itération, le cadre de is_reverse est illustré à la figure 8.2.
J'ai pris une licence en organisant les variables dans le cadre et en ajoutant des lignes pointillées pour montrer
que les valeurs de i et j indiquent des caractères dans word1 et word2.
À partir de ce diagramme, lancez le programme sur papier en changeant les valeurs de i et j
lors de chaque itération. Recherchez et corrigez la deuxième erreur dans cette fonction.

8.12. Glossaire

79
word1
i

’pots’
0

word2

’stop’
j

3

Figure 8.2: Diagramme d'état.

8.12

Glossaire

objet: quelque chose auquel une variable peut se référer. Pour l'instant, vous pouvez utiliser "objet" et "valeur"
indifféremment.
sequence: Collection ordonnée de valeurs où chaque valeur est identifiée par un entier
indice.
item: Une des valeurs d'une séquence.
index: valeur entière utilisée pour sélectionner un élément dans une séquence, tel qu'un caractère dans une chaîne.
Dans Python, les index commencent à 0.
slice: partie d'une chaîne spécifiée par une plage d'indices.
Chaîne vide: Chaîne sans caractères et longueur 0, représentée par deux guillemets
des notes.
immutable: La propriété d'une séquence dont les éléments ne peuvent pas être modifiés.
traverse: pour parcourir les éléments d'une séquence, en effectuant une opération similaire sur
chaque.
search: Un modèle de parcours qui s'arrête lorsqu'il trouve ce qu'il cherche.
counter: variable utilisée pour compter quelque chose, généralement initialisée à zéro puis incrémentée.
invocation: une instruction qui appelle une méthode.
argument optionnel: argument de fonction ou de méthode non requis.

8.13

Des exercices

Exercice 8.1. Lisez la documentation des méthodes de chaîne à l'adresse http: // docs. python. org / 3 /
bibliothèque / stdtypes. html # string-methods. Vous pourriez vouloir expérimenter avec certains d'entre eux
pour vous assurer que vous comprenez comment ils fonctionnent. strip et replace sont particulièrement utiles.
La documentation utilise une syntaxe qui peut être source de confusion.
Par exemple, dans
find (sub [, start [, end]]), les crochets indiquent des arguments facultatifs. Donc sub est requis, mais
start est optionnel, et si vous incluez start, alors end est optionnel.
Exercice 8.2. Il existe une méthode de chaîne appelée count qui est similaire à la fonction de la section 8.7.
Lisez la documentation de cette méthode et écrivez une invocation qui compte le nombre de
'banane'.
Exercice 8.3. Une tranche de chaîne peut prendre un troisième index qui spécifie la "taille de pas"; c'est-à-dire le nombre
des espaces entre les caractères successifs. Un pas de 2 signifie tous les autres caractères; 3 signifie tous les
troisième, etc.

80

Chapitre 8. Chaînes

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
Une taille de pas de -1 traverse le mot en arrière, de sorte que la tranche [:: - 1] génère une chaîne inversée.
Utilisez cet idiome pour écrire une version d'une ligne de is_palindrome à partir de l'exercice 6.3.
Exercice 8.4. Les fonctions suivantes sont toutes destinées à vérifier si une chaîne contient des
lettres minuscules, mais au moins certaines d'entre elles sont fausses. Pour chaque fonction, décrivez ce que la fonction
fait (en supposant que le paramètre est une chaîne).

def any_lowercase1(s):
for c in s:
if c.islower():
return True
else:
return False
def any_lowercase2(s):
for c in s:
if 'c'.islower():
return 'True'
else:
return 'False'
def any_lowercase3(s):
for c in s:
flag = c.islower()
return flag
def any_lowercase4(s):
flag = False
for c in s:
flag = flag or c.islower()
return flag
def any_lowercase5(s):
for c in s:
if not c.islower():
return False
return True
Exercice 8.5. Un cryptage César est une forme de cryptage faible qui consiste à "faire tourner" chaque lettre de
un nombre fixe de places. Faire pivoter une lettre signifie la déplacer dans l’alphabet
au début si nécessaire, 'A' pivoté de 3 est 'D' et 'Z' tourné de 1 est 'A'.
Pour faire pivoter un mot, faites pivoter chaque lettre du même montant. Par exemple, "cheer" pivoté de 7 est "jolly"
et "melon" tourné de -10 est "cubed". Dans le film 2001: Odyssée de l'espace, l'ordinateur de bord
est appelée HAL, qui est tournée de -1 par IBM.
Ecrire une fonction appelée rotate_word qui prend une chaîne et un entier comme paramètres et renvoie
une nouvelle chaîne contenant les lettres de la chaîne d'origine pivotée par la quantité donnée.
Vous voudrez peut-être utiliser la fonction intégrée ord, qui convertit un caractère en code numérique, et

8.13. Des exercices

81

chr, qui convertit les codes numériques en caractères. Les lettres de l'alphabet sont codées par ordre alphabétique
ordre, par exemple:
>>> ord ('c') - ord ('a')
2
Parce que "c" est la lettre de deux éthiques de l'alphabet. Mais attention: les codes numériques pour les majuscules
les lettres sont différentes.
Les blagues potentiellement choquantes sur Internet sont parfois encodées dans ROT13, qui est une César
cypher avec rotation 13. Si vous n'êtes pas facilement offensé, trouvez et décodez certains d'entre eux. Solution:
http: // thinkpython2. com / code / rotate. py.

82

Chapitre 8. ChaînesChapitre 9

Cas d'étude: jeu de mots
Ce chapitre présente la deuxième cas d'étude, qui consiste à résoudre des énigmes de mots en
rechercher des mots qui ont certaines propriétés. Par exemple, nous trouverons les palindromes les plus longs en anglais et rechercherons des mots dont les lettres apparaissent dans l’ordre alphabétique. Et
Je présenterai un autre plan de développement de programme: réduction à un problème déjà résolu.

9.1

Lecture de listes de mots

Pour les exercices de ce chapitre, nous avons besoin d'une liste de mots anglais. Il y a beaucoup de mot
listes disponibles sur le Web, mais celle qui convient le mieux à notre objectif est l'une des listes de mots
collecté et contribué au domaine public par Grady Ward dans le cadre du projet de lexique Moby (voir http://wikipedia.org/wiki/Moby_Project). C'est une liste de 113 809 mots croisés
officiels; c'est-à-dire des mots considérés comme valides dans les mots croisés et autres jeux de
mots. Dans la collection Moby, le nom de fichier est 113809of.fic; vous pouvez télécharger une copie,
avec le simple nom words.txt, de http://thinkpython2.com/code/words.txt.
Ce fichier est en texte brut, vous pouvez donc l'ouvrir avec un éditeur de texte, mais vous pouvez également le lire à partir de
Python. La fonction intégrée open prend le nom du fichier comme paramètre et retourne un
objet fichier que vous pouvez utiliser pour lire le fichier.

>>> fin = open('words.txt')
fin est un nom commun pour un objet fichier utilisé pour la saisie. L'objet de fichier fournit plusieurs
méthodes pour lire, y compris readline, qui lit les caractères du fichier jusqu'à ce qu'il soit
à une nouvelle ligne et renvoie le résultat sous forme de chaîne:
>>> fin.readline()
'aa\r\n'
Le premier mot de cette liste est "aa", qui est une sorte de lave. La séquence \ r \ n
représente deux caractères d'espacement, un retour chariot et une nouvelle ligne, qui séparent cette
mot du suivant.
L’objet fichier garde une trace de son emplacement dans le fichier, donc si vous appelez à nouveau readline, vous obtenez
le mot suivant:

84

Chapitre 9. Etude de cas: jeux de mots

>>> fin.readline()
'aah\r\n'
Le mot suivant est "aah", qui est un mot parfaitement légitime, alors arrête de me regarder comme
ça. Ou, si c'est le blanc qui vous dérange, on peut s'en débarrasser avec un string
bande de méthode:
>>> line = fin.readline()
>>> word = line.strip()
>>> word
'aahed'
Vous pouvez également utiliser un objet fichier dans le cadre d'une boucle for. Ce programme lit words.txt et
imprime chaque mot, un par ligne:
fin = open('words.txt')
for line in fin:
word = line.strip()
print(word)

9.2

Des exercices

Il y a des solutions à ces exercices dans la section suivante. Vous devriez au moins essayer chacun
un avant de lire les solutions.
Exercice 9.1. Ecrire un programme qui lit des mots.txt et imprime seulement les mots avec plus de 20
caractères (sans compter les espaces).
Exercice 9.2. En 1939, Ernest Vincent Wright a publié un roman de 50 000 mots intitulé Gadsby
ne contient pas la lettre "e". Puisque "e" est la lettre la plus courante en anglais, ce n'est pas facile de
faire.
En fait, il est difficile de construire une pensée solitaire sans utiliser ce symbole le plus commun. C'est
ralentir au début, mais avec prudence et des heures d'entraînement, vous pouvez progressivement gagner de la facilité.
D'accord, je vais m'arrêter maintenant.
Ecrivez une fonction appelée has_no_e qui renvoie True si le mot donné n'a pas la lettre "e" dans
il.
Modifiez votre programme à partir de la section précédente pour n'imprimer que les mots sans "e" et calculez le pourcentage des mots de la liste sans "e".
Exercice 9.3. Ecrire une fonction nommée évite qui prend un mot et une chaîne de lettres interdites,
et qui renvoie True si le mot n'utilise aucune des lettres interdites.
Modifiez votre programme pour inviter l'utilisateur à entrer une chaîne de lettres interdites, puis imprimez le
nombre de mots qui n'en contiennent aucun. Pouvez-vous trouver une combinaison de 5 lettres interdites
cela exclut le plus petit nombre de mots?
Exercice 9.4. Écrivez une fonction nommée uses_only qui prend un mot et une chaîne de lettres, et
qui renvoie True si le mot ne contient que des lettres dans la liste. Pouvez-vous faire une phrase en utilisant seulement
les lettres acefhlo? Autre que "Hoe alfalfa?"
Exercice 9.5. Écrivez une fonction nommée uses_all qui prend un mot et une chaîne de lettres requises,
et qui renvoie True si le mot utilise toutes les lettres requises au moins une fois. Combien de mots sont
là qui utilisent toutes les voyelles aeiou? Pourquoi pas aeiouy?
Exercice 9.6. Ecrire une fonction appelée is_abecedarian qui renvoie True si les lettres d'un mot
apparaissent dans l'ordre alphabétique (les lettres doubles sont correctes). Combien de mots abecedarian y a-t-il?

9.3. Chercher

9.3

85

Chercher

Tous les exercices de la section précédente ont quelque chose en commun. ils peuvent être résolus
avec le modèle de recherche que nous avons vu dans la section 8.6. L'exemple le plus simple est:

def has_no_e(word):
for letter in word:
if letter == 'e':
return False
return True
La boucle for traverse les caractères du mot. Si nous trouvons la lettre "e", nous pouvons immédiatement
retourner faux; sinon nous devons passer à la lettre suivante. Si nous quittons la boucle normalement, cela
signifie que nous n'avons pas trouvé de "e", donc nous retournons True.
Vous pourriez écrire cette fonction de manière plus concise en utilisant l'opérateur in, mais j'ai commencé avec cette
version car elle démontre la logique du modèle de recherche.

Avoids est une version plus générale de has_no_e mais elle a la même structure:
def avoids(word, forbidden):
for letter in word:
if letter in forbidden:
return False
return True
Nous pouvons retourner Faux dès que nous trouvons une lettre interdite; si nous arrivons à la fin de la boucle,
nous retournons True.
uses_only est similaire sauf que le sens de la condition est inversé:
ef uses_only(word, available):
for letter in word:
if letter not in available:
return False
return True
Au lieu d'une liste de lettres interdites, nous avons une liste de lettres disponibles. Si nous trouvons une lettre dans
mot qui n'est pas disponible, nous pouvons retourner Faux.
uses_all est similaire sauf que nous inversons le rôle du mot et de la chaîne de lettres:
def uses_all (mot, requis):
pour lettre en requis:
si lettre pas en mot:
retourner faux
retourne True
Au lieu de parcourir les lettres du mot, la boucle parcourt les lettres requises. Si l'un des
les lettres requises n'apparaissent pas dans le mot, nous pouvons retourner Faux.
Si vous pensiez vraiment comme un informaticien, vous auriez reconnu que
uses_all était une instance d'un problème déjà résolu, et vous auriez écrit:

def uses_all(word, required):
return uses_only(required, word)
Ceci est un exemple de plan de développement de programme appelé réduction à un problème déjà résolu
problème, ce qui signifie que vous reconnaissez le problème sur lequel vous travaillez en tant qu'instance
d'un problème résolu et appliquer une solution existante.

86

9.4

Chapitre 9. Etude de cas: jeux de mots

Boucler avec des indices

J'ai écrit les fonctions dans la section précédente avec pour les boucles parce que je n'avais besoin que de la
personnages dans les cordes; Je n'ai rien eu à faire avec les indices.
Pour is_abecedarian nous devons comparer les lettres adjacentes, ce qui est un peu difficile avec un for
boucle:

def is_abecedarian(word):
previous = word[0]
for c in word:
if c < previous:
return False
previous = c
return True
Une alternative consiste à utiliser la récursivité:

def is_abecedarian(word):
if len(word) <= 1:
return True
if word[0] > word[1]:
return False
return is_abecedarian(word[1:])
Une autre option consiste à utiliser une boucle while:

def is_abecedarian(word):
i = 0
while i < len(word)-1:
if word[i+1] < word[i]:
return False
i = i+1
return True
La boucle commence à i = 0 et se termine lorsque i = len (mot) -1. A chaque fois dans la boucle, il compare le caractère i (que vous pouvez considérer comme le personnage actuel) au i + 1
personnage (que vous pouvez penser comme le suivant).
Si le caractère suivant est inférieur à (alphabétiquement avant) le caractère actuel, alors nous avons découvert une rupture dans la tendance abécédaire, et nous renvoyons Faux.
Si nous arrivons à la fin de la boucle sans trouver de défaut, le mot passe le test. À
convainquez-vous que la boucle se termine correctement, considérez un exemple comme «flossy». le
la longueur du mot est 6, donc la dernière fois que la boucle s'exécute est quand je est 4, qui est l'index de
le dernier caractère. Lors de la dernière itération, il compare le dernier caractère
au dernier, qui est ce que nous voulons.
Voici une version de is_palindrome (voir exercice 6.3) qui utilise deux index; on commence à
le début et monte; l'autre commence à la fin et descend.

def is_palindrome(word):
i = 0
j = len(word)-1
while i<j:
if word[i] != word[j]:

9.5. Le débogage

87

return False
i = i+1
j = j-1
return True
Ou nous pourrions réduire à un problème déjà résolu et écrire:

def is_palindrome (mot):
return is_reverse (mot, mot)
Utiliser is_reverse de la section 8.11.

9,5

Le débogage

Les programmes de test sont difficiles. Les fonctions de ce chapitre sont relativement faciles à tester car
vous pouvez vérifier les résultats à la main. Malgré cela, il est difficile et impossible de choisir un ensemble de mots qui teste toutes les erreurs possibles.
En prenant has_no_e comme exemple, il y a deux cas évidents à vérifier: les mots qui ont un
'E' devrait renvoyer False et les mots qui ne le sont pas devraient retourner True. Vous ne devriez pas avoir
difficulté à trouver un de chacun.
Dans chaque cas, il existe des sous-casques moins évidents. Parmi les mots qui ont un
"E", vous devriez tester les mots avec un "e" au début, à la fin et quelque part dans le
milieu. Vous devriez tester des mots longs, des mots courts et des mots très courts, comme le vide
chaîne. La chaîne vide est un exemple d'un cas particulier, qui est l'un des non évidents
cas où des erreurs se cachent souvent.
En plus des cas de test que vous générez, vous pouvez également tester votre programme avec une liste de mots.
comme words.txt. En scannant la sortie, vous pourrez peut-être intercepter des erreurs, mais faites attention:
vous pourriez attraper un type d'erreur (mots qui ne devraient pas être inclus, mais sont) et non
un autre (les mots qui devraient être inclus, mais ne le sont pas).
En général, les tests peuvent vous aider à trouver des bogues, mais il n’est pas facile de générer un bon ensemble de
cas de test, et même si vous le faites, vous ne pouvez pas être sûr que votre programme est correct. Selon un
informaticien légendaire:
Les tests de programme peuvent être utilisés pour montrer la présence de bogues, mais jamais pour montrer
leur absence!
- Edsger W. Dijkstra

9,6

Glossaire

objet fichier: valeur représentant un fichier ouvert.
réduction à un problème déjà résolu: une façon de résoudre un problème en l'exprimant
comme exemple d'un problème déjà résolu.
cas particulier: un cas de test atypique ou non évident (et moins susceptible d'être traité correctement).

88

9,7

Chapitre 9. Etude de cas: jeux de mots

Des exercices

Exercice 9.7. Cette question est basée sur un Puzzler qui a été diffusé sur le programme radio Car
Talk (http: // www. Cartalk. Com / content / puzzlers):
Donnez-moi un mot avec trois lettres doubles consécutives. Je vais vous donner quelques mots
qui se qualifient presque, mais pas. Par exemple, le mot comité, c-o-m-m-i-t-t-e-e. Il
serait génial, sauf pour le "i" qui se glisse là-bas. Ou Mississippi: M-i-s-s-je-s-s-ip-p-i. Si vous pouviez sortir ces choses, ça marcherait. Mais il y a un mot qui a trois
paires de lettres consécutives et, à ma connaissance, cela peut être le seul mot.
Bien sûr, il y en a probablement 500 de plus mais je ne peux que penser à un. Quel est le mot?
Ecrivez un programme pour le trouver. Solution: http: // thinkpython2. com / code / cartalk1. py.
Exercice 9.8. Voici un autre Car Talk Puzzler (http: // www. Cartalk. Com / content /
puzzlers):
"Je conduisais sur l’autoroute l’autre jour et j’ai remarqué mon odomètre.
Comme la plupart des odomètres, il affiche six chiffres, en miles entiers seulement. Donc, si ma voiture avait 300 000
miles, par exemple, je verrais 3-0-0-0-0-0.
"Maintenant, ce que j'ai vu ce jour-là était très intéressant. J'ai remarqué que les 4 derniers chiffres étaient
palindromique; c'est-à-dire qu'ils lisent le même vers l'avant que vers l'arrière. Par exemple, 5-4-4-5 est un
palindrome, donc mon odomètre aurait pu lire 3-1-5-4-4-5.
"Un mile plus tard, les 5 derniers numéros étaient palindromiques. Par exemple, il aurait pu lire
3-6-5-4-5-6. Un kilomètre après, les 4 numéros sur 6 étaient au centre. Et
tu es prêt pour ça? Un mile plus tard, tous les 6 étaient palindromiques!
"La question est: qu'est-ce qui était au compteur lorsque j'ai regardé pour la première fois?"
Ecrire un programme Python qui teste tous les nombres à six chiffres et imprime les nombres qui satisfont
ces exigences. Solution: http: // thinkpython2. com / code / cartalk2. py.
Exercice 9.9. Voici un autre Car Talk Puzzler que vous pouvez résoudre en effectuant une recherche (http: // www.
cartalk. com / content / puzzlers):
"Récemment j'ai eu une visite avec ma mère et nous avons réalisé que les deux chiffres qui font
mon âge quand inversé abouti à son âge. Par exemple, si elle a 73 ans, je suis 37. Nous
me demandais combien de fois cela se passait au fil des ans mais nous nous sommes égarés avec d'autres
sujets et nous n'avons jamais trouvé de réponse.
"Quand je suis rentré à la maison, j'ai compris que les chiffres de nos âges ont été réversibles six fois
jusque là. J'ai aussi compris que si nous avions de la chance, cela se reproduirait dans quelques années et
Si nous avons vraiment de la chance, cela se produira encore une fois après cela. En d'autres termes, il serait
est arrivé 8 fois au total. Donc, la question est: quel âge ai-je maintenant? "
Ecrivez un programme Python qui recherche des solutions à ce Puzzler. Astuce: vous pourriez trouver la méthode de 
chaîne zfill utile.Chapitre 10

Lists
Ce chapitre présente l'un des types de données les plus utiles de Python. Vous apprendrez aussi
plus sur les objets et ce qui peut arriver quand vous avez plus d'un nom pour le même
objet.

10.1

List est une séquence

Comme une chaîne, une liste est une suite de valeurs. Dans une chaîne, les valeurs sont des caractères; dans une liste,
ils peuvent être de n'importe quel type. Les valeurs d'une liste sont appelées des éléments ou parfois des items.
Il existe plusieurs façons de créer une nouvelle liste. le plus simple est d'inclure les éléments dans le carré
parenthèses ([ et ]):

[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
Le premier exemple est une liste de quatre nombres entiers. La seconde est une liste de trois chaînes. Les éléments
d'une liste ne doivent pas nécessairement être du même type. La liste suivante contient une chaîne, un float, un
entier, et (tada!) une autre liste:

['spam', 2.0, 5, [10, 20]]
Une liste dans une autre liste est imbriquée.
Une liste ne contenant aucun élément s'appelle une liste vide; vous pouvez en créer un avec des []
vides, [].
Comme vous vous en doutez, vous pouvez affecter des valeurs de liste aux variables:

>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> numbers = [42, 123]
>>> empty = []
>>> print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []

90

Chapitre 10. Listes
liste
les fromages

0

'Cheddar'

1

'Edam'

2

'Gouda'

0

42

1

123

liste
Nombres

5
liste
vide

Figure 10.1: Diagramme d'état.

10.2

Les listes sont mutables

La syntaxe pour accéder aux éléments d'une liste est la même que pour accéder aux caractères
d'un string-le symbole []. L'expression entre crochets spécifie l'index.
Rappelez-vous que les indices commencent à 0:
>>> cheeses[0]
'Cheddar'
Contrairement aux chaînes, les listes sont modifiables. Lorsque l'opérateur de la parenthèse apparaît à gauche d'un
affectation, il identifie l'élément de la liste qui sera affecté.
>>> numbers = [42, 123]
>>> numbers[1] = 5
>>> numbers
[42, 5]
L'élément one-eth des nombres, autrefois 123, est maintenant 5.
La figure 10.1 montre le diagramme d'état pour les fromages, les nombres et vide:
Les listes sont représentées par des cases contenant le mot "list" en dehors et les éléments de la liste
à l'intérieur. les fromages se réfèrent à une liste de trois éléments indexés 0, 1 et 2. les nombres contiennent
deux éléments; le diagramme montre que la valeur du second élément a été réaffectée
de 123 à 5. vide fait référence à une liste sans éléments.
Les index de liste fonctionnent de la même manière que les index de chaîne:
• Toute expression entière peut être utilisée comme index.
• Si vous essayez de lire ou d’écrire un élément qui n’existe pas, vous obtenez une erreur IndexError.
• Si un index a une valeur négative, il compte à rebours depuis la fin de la liste.
L'opérateur in fonctionne également sur les listes.
>>> cheeses = ['Cheddar', 'Edam', 'Gouda']
>>> 'Edam' in cheeses
True
>>> 'Brie' in cheeses
False

10.3. Traverser une liste

10.3

91

Traverser une liste

La manière la plus courante de parcourir les éléments d'une liste est d'utiliser une boucle for. La syntaxe est
le même que pour les chaînes:

for cheese in cheeses:
print(cheese)
Cela fonctionne bien si vous avez seulement besoin de lire les éléments de la liste. Mais si tu veux écrire
ou mettre à jour les éléments, vous avez besoin des index. Une manière commune de le faire est de combiner les
fonctions intégrées range et len:

for i in range(len(numbers)):
numbers[i] = numbers[i] * 2
Cette boucle parcourt la liste et met à jour chaque élément. len renvoie le nombre d'éléments
dans la liste. range renvoie une liste d'indices de 0 à n - 1, où n est la longueur de la liste.
Chaque fois que je traverse la boucle, j'obtiens l'index de l'élément suivant. La déclaration d'affectation
dans le corps utilise i pour lire l'ancienne valeur de l'élément et attribuer la nouvelle valeur.
Une boucle for sur une liste vide ne lance jamais le corps:

for x in []:
print('This never happens.')
Bien qu'une liste puisse contenir une autre liste, la liste imbriquée compte toujours comme un seul élément. le
La longueur de cette liste est de quatre:

['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]

10.4

Opérations de liste

L'opérateur + concatène les listes:

>>>
>>>
>>>
>>>
[1,

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c
2, 3, 4, 5, 6]

L'opérateur * répète une liste un nombre de fois donné:

>>>
[0,
>>>
[1,

[0] * 4
0, 0, 0]
[1, 2, 3] * 3
2, 3, 1, 2, 3, 1, 2, 3]

Le premier exemple se répète quatre fois. Le deuxième exemple répète la liste [1, 2, 3]
trois fois.

10,5

tranches de List (List slices)

L'opérateur de tranche travaille également sur des listes:

92

Chapitre 10. Listes

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
Si vous omettez le premier index, la tranche commence au début. Si vous omettez le second, la tranche
va à la fin. Donc, si vous omettez les deux, la tranche est une copie de la liste complète.

>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
Comme les listes sont modifiables, il est souvent utile de faire une copie avant d'effectuer des opérations
modifier des listes.
Un opérateur de tranche à gauche d'une affectation peut mettre à jour plusieurs éléments:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> t
['a', 'x', 'y', 'd', 'e', 'f']

10.6

Méthodes de liste

Python fournit des méthodes qui fonctionnent sur les listes. Par exemple, append ajoute un nouvel élément
à la fin d'une liste:

>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> t
['a', 'b', 'c', 'd']
extend prend une liste comme argument et ajoute tous les éléments:
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> t1
['a', 'b', 'c', 'd', 'e']
Cet exemple laisse t2 non modifié.

trier les éléments de la liste de bas en haut:
>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> t
['a', 'b', 'c', 'd', 'e']
La plupart des méthodes de liste sont nulles; ils modifient la liste et renvoient None. Si vous écrivez accidentellement
t = t.sort(), vous serez déçu du résultat.

10.7. Map, filter et reduce

10,7

93

Map, filter et reduce

Pour additionner tous les numéros d'une liste, vous pouvez utiliser une boucle comme celle-ci:

def add_all(t):
total = 0
for x in t:
total += x
return total
total est initialisé à 0. Chaque fois que la boucle est terminée, x obtient un élément de la liste.
L'opérateur + = fournit un moyen rapide de mettre à jour une variable. Cette affectation augmentée
déclaration,
total + = x
est équivalent à

total = total + x
Au fur et à mesure que la boucle s'exécute, total cumule la somme des éléments; une variable utilisée de cette façon est
parfois appelé un accumulateur.
L’ajout des éléments d’une liste est une opération si courante que Python
fonction intégrée, somme:

>>> t = [1, 2, 3]
>>> sum(t)
6
Une opération comme celle-ci qui combine une séquence d'éléments en une seule valeur est parfois appelée reduce.
Parfois, vous voulez parcourir une liste tout en en construisant une autre. Par exemple, la fonction
suivante prend une liste de chaînes et renvoie une nouvelle liste contenant des chaînes en majuscule:

def capitalize_all(t):
res = []
for s in t:
res.append(s.capitalize())
return res
res est initialisé avec une liste vide; chaque fois que nous parcourons la boucle, nous ajoutons l'élément suivant. Donc res est un autre type d'accumulateur.
Une opération comme capitalise_all est parfois appelée map car elle "mappe" une fonction
(dans ce cas la méthode capitalise) sur chacun des éléments d'une séquence.
Une autre opération courante consiste à sélectionner certains des éléments d'une liste et à renvoyer une sous-liste.
Par exemple, la fonction suivante prend une liste de chaînes et renvoie une liste contenant
seules les chaînes majuscules:

def only_upper(t):
res = []
for s in t:
if s.isupper():
res.append(s)
return res

94

Chapitre 10. Lists

isupper est une méthode de chaîne qui renvoie True si la chaîne ne contient que des majuscules.
Une opération comme only_upper est appelée filtre car elle sélectionne certains éléments et
filtre les autres.
La plupart des opérations de liste communes peuvent être exprimées sous la forme d'une combinaison de carte, de filtre et de réduction.

10.8

Supprimer des éléments

Il existe plusieurs façons de supprimer des éléments d’une liste. Si vous connaissez l'index de l'élément
vous voulez, vous pouvez utiliser pop:
>>> t = ['a', 'b', 'c']
>>> x = t.pop (1)
>>> t
['a', 'c']
>>> x
'b'
pop modifie la liste et renvoie l'élément qui a été supprimé. Si vous ne fournissez pas de
index, il supprime et retourne le dernier élément.
Si vous n'avez pas besoin de la valeur supprimée, vous pouvez utiliser l'opérateur del:
>>> t = ['a', 'b', 'c']
>>> del t [1]
>>> t
['a', 'c']
Si vous connaissez l'élément que vous souhaitez supprimer (mais pas l'index), vous pouvez utiliser remove:
>>> t = ['a', 'b', 'c']
>>> t.remove ('b')
>>> t
['a', 'c']
La valeur de retour de remove est None.
Pour supprimer plusieurs éléments, vous pouvez utiliser del avec un index de tranche:
>>> t = ['a', 'b', 'c', 'd', 'e', ​​'f']
>>> del t [1: 5]
>>> t
['un F']
Comme d'habitude, la tranche sélectionne tous les éléments jusqu'au deuxième index, mais sans l'inclure.

10,9

Listes et chaînes

Une chaîne est une suite de caractères et une liste est une suite de valeurs, mais une liste de caractères
n'est pas la même chose qu'une chaîne. Pour convertir une chaîne en une liste de caractères, vous pouvez utiliser list():

>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']

10.10. Objets et valeurs

95
une

'banane'

une

b

'banane'

b

'banane'

Figure 10.2: Diagramme d'état.
Parce que list est le nom d'une fonction intégrée, évitez de l'utiliser comme une variable
prénom. J'évite aussi l parce que ça ressemble trop à 1. Donc c'est pour ça que j'utilise t.
La fonction de liste divise une chaîne en lettres individuelles. Si vous voulez casser une chaîne dans
mots, vous pouvez utiliser la méthode split:

>>> s = 'pining for the fjords'
>>> t = s.split()
>>> t
['pining', 'for', 'the', 'fjords']
Un argument facultatif appelé délimiteur spécifie les caractères à utiliser comme limites de mot. L'exemple suivant utilise un trait d'union comme délimiteur:

>>> s = 'spam-spam-spam'
>>> delimiter = '-'
>>> t = s.split(delimiter)
>>> t
['spam', 'spam', 'spam']
join est l'inverse de split. Il prend une liste de chaînes et concatène les éléments. rejoindre est
une méthode de chaîne, vous devez donc l'invoquer sur le délimiteur et passer la liste en paramètre:
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
Dans ce cas, le délimiteur est un caractère d'espacement, alors la jointure place un espace entre les mots. À
concaténer des chaînes sans espaces, vous pouvez utiliser la chaîne vide '' comme délimiteur.

10.10

Objets et valeurs

Si nous exécutons ces instructions d'affectation:

a = 'banana'
b = 'banana'
Nous savons que a et b se réfèrent tous deux à une chaîne, mais nous ne savons pas s’ils font référence à la chaîne.
même chaîne. Il y a deux états possibles, illustrés à la Figure 10.2.
Dans un cas, a et b se réfèrent à deux objets différents qui ont la même valeur. Dans la seconde
cas, ils se rapportent au même objet.
Pour vérifier si deux variables font référence au même objet, vous pouvez utiliser l'opérateur is.

96

Chapitre 10. Listes
une

[1, 2, 3]

b

[1, 2, 3]

Figure 10.3: Diagramme d'état.
une
b

[1, 2, 3]

Figure 10.4: Diagramme d'état.

>>> a = 'banana'
>>> b = 'banana'
>>> a is b
True
Dans cet exemple, Python n'a créé qu'un seul objet de chaîne, et les deux a et b s'y réfèrent. Mais
Lorsque vous créez deux listes, vous obtenez deux objets:

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False
Donc, le diagramme d'état ressemble à la Figure 10.3.
Dans ce cas, nous dirions que les deux listes sont équivalentes, car elles ont les mêmes éléments, mais pas identiques, car elles ne sont pas le même objet. Si deux objets sont identiques,
ils sont également équivalents, mais s'ils sont équivalents, ils ne sont pas nécessairement identiques.
Jusqu'à présent, nous avons utilisé "objet" et "valeur" de manière interchangeable, mais c'est plus précis
dire qu'un objet a une valeur. Si vous évaluez [1, 2, 3], vous obtenez un objet liste dont
value est une suite d'entiers. Si une autre liste comporte les mêmes éléments, nous disons qu’elle a les mêmes
même valeur, mais ce n'est pas le même objet.

10.11

Aliasing

Si a fait référence à un objet et que vous affectez b = a, les deux variables font référence au même objet:

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
Le diagramme d'état ressemble à la Figure 10.4.
L'association d'une variable avec un objet s'appelle une référence. Dans cet exemple, il y a
deux références au même objet.
Un objet avec plus d'une référence a plus d'un nom, nous disons donc que l'objet
est aliasé.
Si l'objet aliasé est mutable, les modifications effectuées avec un alias affectent l'autre:

10.12. Liste des arguments

97
__principale__
delete_head

des lettres
t

liste
0

'une'

1

'B'

2

'C'

Figure 10.5: Diagramme de pile.

>>> b [0] = 42
>>> a
[42, 2, 3]
Bien que ce comportement puisse être utile, il est sujet aux erreurs. En général, il est plus prudent d'éviter
aliasing lorsque vous travaillez avec des objets mutables.
Pour les objets immuables tels que les chaînes de caractères, l'aliasing n'est pas un problème. Dans cet exemple:

a = 'banane'
b = 'banane'
Il ne fait presque jamais de différence si a et b se réfèrent ou non à la même chaîne.

10.12

Liste des arguments

Lorsque vous passez une liste à une fonction, la fonction obtient une référence à la liste. Si la fonction
modifie la liste, l'appelant voit le changement. Par exemple, delete_head supprime le premier
élément d'une liste:

def delete_head (t):
del t [0]
Voici comment il est utilisé:

>>> letters = ['a', 'b', 'c']
>>> delete_head(letters)
>>> letters
['b', 'c']
Le paramètre t et les lettres variables sont des alias pour le même objet. Le diagramme de la pile
ressemble à la figure 10.5.
Puisque la liste est partagée par deux cadres, je l’ai dessiné entre eux.
Il est important de distinguer les opérations qui modifient les listes et les opérations qui créent de nouvelles listes. Par exemple, la méthode append modifie une liste, mais l'opérateur + crée un
nouvelle liste.
Voici un exemple utilisant append:

>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None

98

Chapitre 10. Listes

La valeur renvoyée par append est None.
Voici un exemple d'utilisation de l'opérateur +:

>>>
>>>
[1,
>>>
[1,

t3 = t1 + [4]
t1
2, 3]
t3
2, 3, 4]

Le résultat de l'opérateur est une nouvelle liste et la liste d'origine reste inchangée.
Cette différence est importante lorsque vous écrivez des fonctions censées modifier des listes.
Par exemple, cette fonction ne supprime pas la tête d'une liste:

def bad_delete_head (t):
t = t [1:]

# FAUX!

L'opérateur de tranche crée une nouvelle liste et l'affectation lui fait référence, mais cela ne
affecter l'appelant (caller).

>>>
>>>
>>>
[1,

t4 = [1, 2, 3]
bad_delete_head (t4)
t4
2,3)

Au début de bad_delete_head, t et t4 se réfèrent à la même liste. A la fin, on se réfère
à une nouvelle liste, mais t4 fait toujours référence à la liste originale, non modifiée.
Une alternative consiste à écrire une fonction qui crée et renvoie une nouvelle liste. Par exemple, la queue
renvoie tout sauf le premier élément d'une liste:

def tail(t):
return t[1:]
Cette fonction laisse la liste d'origine non modifiée. Voici comment il est utilisé:

>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> rest
['b', 'c']

10.13

Le débogage

L'utilisation imprudente de listes (et d'autres objets mutables) peut entraîner de longues heures de débogage. Ici
sont des pièges courants et des moyens de les éviter:
1. La plupart des méthodes de liste modifient l'argument et renvoient None. C'est le contraire du
méthodes de chaîne, qui renvoient une nouvelle chaîne et laissent l’original
Si vous avez l'habitude d'écrire du code chaîne comme celui-ci:

word = word.strip()
Il est tentant d’écrire un code de liste comme celui-ci:

10.13. Le débogage

t = t.sort ()

99

# FAUX!

Étant donné que sort renvoie None, la prochaine opération que vous effectuez avec t risque d'échouer.
Avant d'utiliser les méthodes de liste et les opérateurs, vous devez lire attentivement la documentation et les tester en mode interactif.
2. Choisissez un idiome et respectez-le.
Une partie du problème avec les listes est qu'il y a trop de façons de faire les choses. Par exemple, pour supprimer un élément d'une liste, vous pouvez utiliser des fonctions pop, remove, del ou même une tranche.
affectation.
Pour ajouter un élément, vous pouvez utiliser la méthode append ou l'opérateur +. En admettant que
t est une liste et x est un élément de liste, ceux-ci sont corrects:

t.append (x)
t = t + [x]
t + = [x]
Et les cancres:

t.append([x])
t = t.append(x)
t + [x]
t = t + x

#
#
#
#

FAUX!
FAUX!
FAUX!
FAUX!

Essayez chacun de ces exemples en mode interactif pour vous assurer que vous comprenez
ce qu'ils font. Notez que seul le dernier provoque une erreur d'exécution; les trois autres sont
juridique, mais ils font la mauvaise chose.
3. Faites des copies pour éviter les alias.
Si vous voulez utiliser une méthode comme sort qui modifie l'argument, mais vous devez
conservez également la liste originale, vous pouvez en faire une copie.

>>>
>>>
>>>
>>>
[3,
>>>
[1,

t = [3, 1, 2]
t2 = t [:]
t2.sort ()
t
1, 2]
t2
2, 3]

Dans cet exemple, vous pouvez également utiliser la fonction intégrée triée, qui renvoie un nouveau,
liste triée et laisse l'original seul.

>>>
>>>
[3,
>>>
[1,

t2 = sorted(t)
t
1, 2]
t2
2, 3]

100

10.14

Chapitre 10. Listes

Glossaire

list: une séquence de valeurs.
element: Une des valeurs d'une liste (ou d'une autre séquence), également appelée éléments.
liste imbriquée: une liste qui est un élément d'une autre liste.
accumulator: Une variable utilisée dans une boucle pour additionner ou accumuler un résultat.
affectation augmentée: instruction qui met à jour la valeur d'une variable à l'aide d'un opérateur tel que + =.
réduire: Un modèle de traitement qui traverse une séquence et accumule les éléments dans
un seul résultat.
map: modèle de traitement qui traverse une séquence et effectue une opération sur chaque
élément.
filter: Un modèle de traitement qui traverse une liste et sélectionne les éléments qui satisfait certains
critères.
objet: quelque chose auquel une variable peut se référer. Un objet a un type et une valeur.
équivalent: avoir la même valeur.
identique: Être le même objet (ce qui implique une équivalence).
reference: Association entre une variable et sa valeur.
aliasing: une circonstance où deux variables ou plus se rapportent au même objet.
délimiteur: caractère ou chaîne utilisé pour indiquer où une chaîne doit être divisée.

10h15

Des exercices

Vous pouvez télécharger des solutions à ces exercices depuis http://thinkpython2.com/code/
list_exercises.py.
Exercice 10.1. Ecrire une fonction appelée nested_sum qui prend une liste de listes d'entiers et additionne
les éléments de toutes les listes imbriquées. Par exemple:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum (t)
21
Exercice 10.2. Ecrire une fonction appelée cumsum qui prend une liste de nombres et retourne la somme cumulée; c'est-à-dire une nouvelle liste où l'élément ith est la somme des premiers i + 1 éléments de la
liste originale. Par exemple:
>>> t = [1, 2, 3]
>>> cumsum (t)
[1, 3, 6]
Exercice 10.3. Ecrivez une fonction appelée middle qui prend une liste et retourne une nouvelle liste contenant
tous sauf le premier et le dernier élément. Par exemple:
>>> t = [1, 2, 3, 4]
>>> milieu (t)
[2, 3]

10h15 Des exercices

101

Exercice 10.4. Ecrire une fonction appelée chop qui prend une liste, la modifie en supprimant le premier
derniers éléments et renvoie None. Par exemple:

>>> t = [1, 2, 3, 4]
>>> chop (t)
>>> t
[2, 3]
Exercice 10.5. Écrivez une fonction appelée is_sorted qui prend une liste comme paramètre et renvoie True
si la liste est triée par ordre croissant et False sinon. Par exemple:
>>> is_sorted ([1, 2, 2])
Vrai
>>> is_sorted (['b', 'a'])
Faux
Exercice 10.6. Deux mots sont des anagrammes si vous pouvez réorganiser les lettres de l'une pour épeler l'autre.
Écrivez une fonction appelée is_anagram qui prend deux chaînes et renvoie True si ce sont des anagrammes.
Exercice 10.7. Ecrire une fonction appelée has_duplicates qui prend une liste et retourne True si
est tout élément qui apparaît plus d'une fois. Il ne doit pas modifier la liste d'origine.
Exercice 10.8. Cet exercice concerne le soi-disant paradoxe de l'anniversaire, sur lequel vous pouvez lire
à http: // fr. Wikipédia. org / wiki / Birthday_ paradox.
S'il y a 23 élèves dans votre classe, quelles sont les chances que deux d'entre vous aient le même anniversaire?
Vous pouvez estimer cette probabilité en générant des échantillons aléatoires de 23 anniversaires et en utilisant des
allumettes. Astuce: vous pouvez générer des anniversaires aléatoires avec la fonction randint du
module random.
Vous pouvez télécharger ma solution à partir de http: // thinkpython2. com / code / anniversaire. py.
Exercice 10.9. Ecrire une fonction qui lit le fichier words.txt et construit une liste avec un élément
par mot Écrivez deux versions de cette fonction, l’une utilisant la méthode append et l’autre utilisant
le idiome t = t + [x]. Lequel prend plus de temps à courir? Pourquoi?
Solution: http: // thinkpython2. com / code / liste de mots. py.
Exercice 10.10. Pour vérifier si un mot figure dans la liste de mots, vous pouvez utiliser l'opérateur in, mais
serait lent car il recherche dans les mots dans l'ordre.
Comme les mots sont dans l’ordre alphabétique, nous pouvons accélérer les choses avec une recherche de bissection (également
connu sous le nom de recherche binaire), qui est similaire à ce que vous faites lorsque vous regardez un mot dans le dictionnaire.
Vous commencez au milieu et vérifiez si le mot que vous recherchez vient avant le mot
au milieu de la liste. Si c'est le cas, vous effectuez la même recherche dans la première moitié de la liste. Sinon vous recherchez
la seconde moitié.
De toute façon, vous réduisez de moitié l'espace de recherche restant. Si la liste de mots comporte 113 809 mots, elle sera
prendre environ 17 étapes pour trouver le mot ou conclure qu'il n'est pas là.
Ecrire une fonction appelée in_bisect qui prend une liste triée et une valeur cible et renvoie l'index
de la valeur dans la liste si elle est là, ou aucun si ce n'est pas.
Ou vous pouvez lire la documentation du module bisect et l'utiliser! Solution: http: //
thinkpython2. com / code / inlist. py.
Exercice 10.11. Deux mots sont une "paire inversée" si chacun est l'inverse de l'autre. Ecrire un programme
qui trouve toutes les paires inverses dans la liste de mots. Solution: http: // thinkpython2. com / code /
paire reverse_ py.
Exercice 10.12. Deux mots "interlock" si l'on prend des lettres en alternance de chacun forme un nouveau
mot. Par exemple, "shoe" et "cold" s'emboîtent pour former "schooled". Solution: http: //

102

Chapitre 10. Listes

thinkpython2. com / code / interlock. py. Crédit: Cet exercice est inspiré par un exemple à
http: // puzzlers. org.
1. Rédigez un programme qui trouve toutes les paires de mots qui s’emboîtent. Astuce: ne pas énumérer toutes les paires!
2. Pouvez-vous trouver des mots à trois voies imbriquées? c'est-à-dire que chaque troisième lettre forme un
mot, à partir du premier, deuxième ou troisième?Chapitre 11

Dictionnaires
Ce chapitre présente un autre type intégré appelé dictionnaire. Les dictionnaires sont l’un des
meilleures fonctionnalités de Python; ils constituent la base de nombreux algorithmes efficaces et élégants.

11.1

Un dictionnaire est une 'mapping' - to be translated

Un dictionnaire est comme une liste, mais plus générale. Dans une liste, les index doivent être des entiers. dans un
dictionnaire, ils peuvent être (presque) n'importe quel type.
Un dictionnaire contient un ensemble d’index, appelés clés, et un ensemble de
valeurs. Chaque clé est associée à une valeur unique. L'association d'une clé et d'une valeur est
appelé une paire clé-valeur ou parfois un élément.
En langage mathématique, un dictionnaire représente un mappage de clés en valeurs, vous permettant
peut également dire que chaque clé correspond à une valeur. Par exemple, nous allons construire un dictionnaire qui
traduit des mots anglais en espagnol, de sorte que les clés et les valeurs sont toutes des chaînes.
La fonction dict crée un nouveau dictionnaire sans éléments. Parce que dict est le nom d'un
fonction intégrée, vous devriez éviter de l’utiliser comme nom de variable.

>>> eng2sp = dict ()
>>> eng2sp
{}
Les crochets, {}, représentent un dictionnaire vide. Pour ajouter des éléments au dictionnaire,
vous pouvez utiliser des crochets:

>>> eng2sp ['one'] = 'uno'
Cette ligne crée un élément qui mappe la clé "one" à la valeur "uno". Si nous imprimons le
dictionnaire, nous voyons une paire clé-valeur avec deux points entre la clé et la valeur:

>>> eng2sp
{'one': 'uno'}
Ce format de sortie est également un format d'entrée. Par exemple, vous pouvez créer un nouveau dictionnaire
avec trois éléments:

104

Chapitre 11. Dictionnaires

>>> eng2sp = {'un': 'uno', 'deux': 'dos', 'trois': 'tres'}
Mais si vous imprimez eng2sp, vous pourriez être surpris:

>>> eng2sp
{'un': 'uno', 'trois': 'tres', 'deux': 'dos'}
L'ordre des paires clé-valeur peut ne pas être le même. Si vous tapez le même exemple
sur votre ordinateur, vous pourriez obtenir un résultat différent. En général, l'ordre des articles dans un
dictionnaire est imprévisible.
Mais ce n’est pas un problème car les éléments d’un dictionnaire ne sont jamais indexés avec des index entiers. A la place, vous utilisez les touches pour rechercher les valeurs correspondantes:

>>> eng2sp ['deux']
'dos'
La clé "deux" correspond toujours à la valeur "dos", donc l'ordre des éléments n'a pas d'importance.
Si la clé ne figure pas dans le dictionnaire, vous obtenez une exception:

>>> eng2sp ['quatre']
KeyError: 'quatre'
La fonction len fonctionne sur les dictionnaires; il retourne le nombre de paires clé-valeur:

>>> len (eng2sp)
3
L'opérateur in travaille également sur les dictionnaires; il vous dit si quelque chose apparaît comme une clé
dans le dictionnaire (apparaître sous forme de valeur ne suffit pas).

>>> 'one' in eng2sp
True
>>> 'uno' in eng2sp
False
Pour voir si quelque chose apparaît comme une valeur dans un dictionnaire, vous pouvez utiliser la méthode
values, qui retourne une collection de valeurs, puis utilise l'opérateur in:

>>> vals = eng2sp.values()
>>> 'uno' in vals
True
L'opérateur in utilise différents algorithmes pour les listes et les dictionnaires. Pour les listes, il cherche dans le
éléments de la liste dans l’ordre, comme dans la section 8.6. À mesure que la liste s'allonge, le temps de recherche devient
plus en proportion directe.
Pour les dictionnaires, Python utilise un algorithme appelé hashtable qui a une propriété remarquable: l'opérateur in prend environ le même temps, quel que soit le nombre d'éléments.
dans le dictionnaire. J'explique comment cela est possible dans la section B.4, mais l'explication pourrait
ne pas faire aucun sens tant que vous n’avez pas lu quelques chapitres supplémentaires.

11.2

Dictionnaire comme une collection de compteurs

Supposons qu'une chaîne vous soit donnée et que vous souhaitiez compter le nombre de fois que chaque lettre apparaît.
Vous pouvez le faire de plusieurs manières:

11.2 Dictionnaire comme une collection de compteurs

105

1. Vous pouvez créer 26 variables, une pour chaque lettre de l'alphabet. Ensuite, vous pouvez traverser la chaîne et, pour chaque caractère, incrémenter le compteur correspondant, probablement en utilisant un conditionnel chaîné.
2. Vous pouvez créer une liste de 26 éléments. Ensuite, vous pouvez convertir chaque lettre en
un numéro (à l'aide de la fonction intégrée ord), utilisez-le comme index dans la liste,
et incrémenter le compteur approprié.
3. Vous pouvez créer un dictionnaire avec des caractères comme clés et des compteurs comme valeurs correspondantes. La première fois que vous voyez un caractère, vous ajouterez un élément au dictionnaire.
Ensuite, vous augmentez la valeur d’un élément existant.
Chacune de ces options effectue le même calcul, mais chacune d’elles implémente
calcul d'une manière différente.
Une implémentation est un moyen d'effectuer un calcul. certaines implémentations sont
mieux que d'autres. Par exemple, un avantage de la mise en œuvre du dictionnaire est que nous
pas besoin de savoir à l’avance quelles lettres apparaissent dans la chaîne et il suffit de
faites de la place pour les lettres qui apparaissent.
Voici à quoi pourrait ressembler le code:

def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d
Le nom de la fonction est histogramm, terme statistique désignant une collection de compteurs.
(ou fréquences).
La première ligne de la fonction crée un dictionnaire vide. La boucle for traverse la chaîne.
A chaque passage dans la boucle, si le caractère (désigné par) c ne figure pas dans le dictionnaire, nous créons un nouvel élément.
avec pour clé c et la valeur initiale 1 (puisque nous avons vu cette lettre une fois). Si c est déjà dans le
dictionnaire on incrémente d[c].
Voici comment ça fonctionne:

>>> h = histogram('brontosaurus')
>>> h
{'a': 1, 'b': 1, 'o': 2, 'n': 1, 's': 2, 'r': 2, 'u': 2, 't': 1}
L'histogramme indique que les lettres "a" et "b" apparaissent une fois; 'o' apparaît deux fois et
ainsi de suite.
Les dictionnaires ont une méthode appelée get qui prend une clé et une valeur par défaut. Si la clé
apparaît dans le dictionnaire, get renvoie la valeur correspondante; sinon il retourne le
valeur par défaut. Par exemple:

>>> h = histogramme ('a')
>>> h
{'a': 1}
>>> h.get ('a', 0)

106

Chapitre 11. Dictionnaires

1
>>> h.get ('b', 0)
0
En tant qu'exercice, utilisez get pour écrire l'histogramme de manière plus concise. Vous devriez pouvoir éliminer
la déclaration si.

11.3

Boucle et dictionnaires

Si vous utilisez un dictionnaire dans une instruction for, il traverse les clés du dictionnaire. Par exemple, print_hist affiche chaque clé et la valeur correspondante:

def print_hist(h):
for c in h:
print(c, h[c])
Voici à quoi ressemble la sortie:
>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1
Encore une fois, les clés ne sont dans aucun ordre particulier. Pour parcourir les clés dans un ordre trié, vous pouvez utiliser
la fonction intégrée triée:
>>> for key in sorted(h):
...
print(key, h[key])
a 1
o 1
p 1
r 2
t 1

11.4

Recherche inversée

Étant donné un dictionnaire d et une clé k, il est facile de trouver la valeur correspondante v = d[k]. Ce
l'opération s'appelle une recherche.
Mais que faire si vous avez v et que vous voulez trouver k? Vous avez deux problèmes: d'abord, il pourrait
avoir plus d'une clé qui correspond à la valeur v. En fonction de l'application, vous pouvez
être capable de choisir un, ou vous devrez peut-être une liste qui les contient tous. Seconde,
il n'y a pas de syntaxe simple pour effectuer une recherche inversée; vous devez rechercher.
Voici une fonction qui prend une valeur et retourne la première clé qui correspond à cette valeur:

def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise LookupError()

11.5 Dictionnaires et listes

107

Cette fonction est un autre exemple du modèle de recherche, mais elle utilise une fonctionnalité que nous n’avons pas
vu auparavant, augmenter. L'instruction de relance provoque une exception. dans ce cas, il provoque une
LookupError, qui est une exception intégrée utilisée pour indiquer qu'une opération de recherche a échoué.
Si nous arrivons à la fin de la boucle, cela signifie que v n’apparaît pas dans le dictionnaire sous forme de valeur.
nous soulevons une exception.
Voici un exemple de recherche inversée réussie:

>>> h = histogram('parrot')
>>> key = reverse_lookup(h, 2)
>>> key
'r'
Et un échec:

>>> key = reverse_lookup(h, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
File "<stdin>", line 5, in reverse_lookup
LookupError
L’effet lorsque vous déclenchez une exception est le même que lorsque Python en déclenche une: il affiche une
traceback et un message d'erreur.
L'instruction de relance peut prendre un message d'erreur détaillé comme argument facultatif. Par exemple:

>>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
Une recherche inversée est beaucoup plus lente qu'une recherche directe; si vous devez le faire souvent, ou si le
dictionnaire devient gros, la performance de votre programme va en souffrir.

11.5

Dictionnaires et listes

Les listes peuvent apparaître sous forme de valeurs dans un dictionnaire. Par exemple, si vous recevez un dictionnaire qui
mappe des lettres aux fréquences, vous voudrez peut-être l’inverser; c'est-à-dire créer un dictionnaire
qui mappe des fréquences aux lettres. Puisqu'il pourrait y avoir plusieurs lettres avec le même
fréquence, chaque valeur du dictionnaire inversé doit être une liste de lettres.
Voici une fonction qui inverse un dictionnaire:

def invert_dict(d):
inverse = dict()
for key in d:
val = d[key]
if val not in inverse:
inverse[val] = [key]
else:
inverse[val].append(key)
return inverse

108

Chapitre 11. Dictionnaires
dict
hist

dict

’a’

1

’p’

inv

list

1

0

’a’

1

1

’p’

’r’

2

2

’t’

’t’

1

3

’o’

’o’

1

0

’r’

list
2

Figure 11.1: Diagramme d'état.
A chaque passage dans la boucle, key obtient une clé de d et val obtient la valeur correspondante.
Si val n’est pas inversé, cela signifie que nous ne l’avons jamais vu auparavant. Nous créons donc un nouvel élément et
initialisez-le avec un singleton (une liste contenant un seul élément). Sinon nous avons vu
cette valeur avant, nous ajoutons donc la clé correspondante à la liste.
Voici un exemple:

>>> hist = histogram('parrot')
>>> hist
{'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
>>> inverse = invert_dict(hist)
>>> inverse
{1: ['a', 'p', 't', 'o'], 2: ['r']}
Le dessin 11.1 est un diagramme d'états montrant hist et inverse. Un dictionnaire est représenté comme un
case avec le type dict dessus et les paires clé-valeur à l'intérieur. Si les valeurs sont des entiers,
floats ou des chaînes, je les dessine à l’intérieur de la boîte, mais je dessine généralement des listes en dehors de la
 boîte, question de garder le schéma simple.
Les listes peuvent être des valeurs dans un dictionnaire, comme le montre cet exemple, mais elles ne peuvent pas être des clés. Voici
Qu'est-ce qui se passe si vous essayez:

>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
File "<stdin>", line 1, in ?
TypeError: list objects are unhashable
J'ai mentionné plus tôt qu'un dictionnaire est mis en œuvre en utilisant une table de hachage et cela signifie que
les clés doivent être hashable.
Un hachage est une fonction qui prend une valeur (de tout type) et renvoie un entier. Dictionnaires
utilisez ces entiers, appelés valeurs de hachage, pour stocker et rechercher des paires clé-valeur.
Ce système fonctionne bien si les clés sont immuables. Mais si les clés sont mutables, comme des listes,
les mauvaises choses arrivent. Par exemple, lorsque vous créez une paire clé-valeur, Python hache la clé
et le stocke à l'emplacement correspondant. Si vous modifiez la clé puis la hachez à nouveau,
irait à un endroit différent. Dans ce cas, vous pourriez avoir deux entrées pour la même clé,
ou vous ne pourrez peut-être pas trouver une clé. De toute façon, le dictionnaire ne fonctionnerait pas correctement.
C’est la raison pour laquelle les clés doivent être remplissables et pourquoi les types mutables comme les listes ne le sont pas. Le plus simple
Pour contourner cette limitation, utilisez des n-uplets, que nous verrons dans le prochain chapitre.

11.6 Mémos

109
fibonacci
n
4

fibonacci
n
3

fibonacci
n
2

fibonacci
n
1

fibonacci
n
1

fibonacci
n
2

fibonacci
n
1

fibonacci
n
0

fibonacci
n
0

Figure 11.2: Graphe d’appel.
Les dictionnaires étant modifiables, ils ne peuvent pas être utilisés comme clés, mais ils peuvent être utilisés comme valeurs.

11.6

Mémos

Si vous avez joué avec la fonction fibonacci de la section 6.7, vous avez peut-être remarqué que
plus l'argument que vous fournissez est grand, plus la fonction met longtemps à s'exécuter. En outre,
le temps d'exécution augmente rapidement.
Pour comprendre pourquoi, considérons la figure 11.2, qui présente le graphe d’appel de fibonacci avec
n = 4:
Un graphique d’appel montre un ensemble de cadres de fonctions, avec des lignes reliant chaque cadre aux cadres.
des fonctions qu'il appelle. En haut du graphique, fibonacci avec n = 4 appelle fibonacci avec
n = 3 et n = 2. À son tour, fibonacci avec n = 3 appelle fibonacci avec n = 2 et n = 1. Etc.
Comptez le nombre de fois où fibonacci (0) et fibonacci (1) sont appelés. C'est un inefficace
solution au problème, et cela s’aggrave à mesure que l’argument s’agrandit.
Une solution consiste à garder une trace des valeurs déjà calculées en les stockant.
dans un dictionnaire. Une valeur calculée précédemment qui est stockée pour une utilisation ultérieure est appelée un mémo.
Voici une version «mémoisée» de fibonacci:

known = {0:0, 1:1}
def fibonacci(n):
if n in known:
return known[n]
res = fibonacci(n-1) + fibonacci(n-2)
known[n] = res
return res
Connu est un dictionnaire qui garde la trace des nombres de Fibonacci que nous connaissons déjà. Il commence
avec deux items: 0 mappe à 0 et 1 mappe à 1.

110

Chapitre 11. Dictionnaires

Chaque fois que Fibonacci est appelé, il vérifie. Si le résultat est déjà là, il peut retourner
immédiatement. Sinon, il doit calculer la nouvelle valeur, l'ajouter au dictionnaire et
rends le.
Si vous utilisez cette version de fibonacci et que vous la comparez à la version originale, vous constaterez que
est beaucoup plus rapide.

11.7

Variables globales

Dans l'exemple précédent, not est créé en dehors de la fonction, il appartient donc à la fonction spécial
appelé __main__. Les variables dans __main__ sont parfois appelées globales car elles
peut être accessible depuis n'importe quelle fonction. Contrairement aux variables locales, qui disparaissent lorsque leur
fonction se termine, les variables globales persistent d'un appel de fonction à l'autre.
Il est courant d'utiliser des variables globales pour les indicateurs. c’est-à-dire des variables booléennes qui indiquent («drapeau»)
si une condition est vraie. Par exemple, certains programmes utilisent un indicateur nommé verbose pour
contrôler le niveau de détail dans la sortie:

verbose = True
def example1():
if verbose:
print('Running example1')
Si vous essayez de réaffecter une variable globale, vous pourriez être surpris. L'exemple suivant est
censé savoir si la fonction a été appelée:

been_called = False
def example2():
been_called = True

# FAUX

Mais si vous l’exécutez, vous verrez que la valeur de been_called ne change pas. Le problème
Est-ce que exemple2 crée une nouvelle variable locale appelée Been_called. La variable locale va
loin lorsque la fonction se termine, et n'a aucun effet sur la variable globale.
Pour réaffecter une variable globale dans une fonction, vous devez déclarer la variable globale avant que
tu l'utilises:

been_called = False
def example2():
global been_called
been_called = True
La déclaration globale dit à l'interprète quelque chose comme: «Dans cette fonction, quand je dis
been_called, je veux dire la variable globale; ne créez pas un local. "
Voici un exemple qui tente de mettre à jour une variable globale:

count = 0
def example3():
count = count + 1
Si vous l'exécutez, vous obtenez:

# FAUX

11.8. Débogage

111

UnboundLocalError: local variable 'count' referenced before assignment
Python suppose que le compte est local et sous cette hypothèse, vous le lisez avant
l'écrire. La solution, encore une fois, est de déclarer le compte global.

def example3():
global count
count += 1
Si une variable globale fait référence à une valeur mutable, vous pouvez modifier la valeur sans déclarer
la variable:

connu = {0: 0, 1: 1}
def example4 ():
connu [2] = 1
Ainsi, vous pouvez ajouter, supprimer et remplacer des éléments d'une liste globale ou d'un dictionnaire, mais si vous le souhaitez
pour réaffecter la variable, vous devez la déclarer:

def example5():
global known
known = dict()
Les variables globales peuvent être utiles, mais si vous en avez beaucoup et que vous les modifiez fréquemment, elles peuvent compliquer le débogage des programmes.

11.8

Débogage

Lorsque vous travaillez avec des jeux de données plus volumineux, il peut être difficile de déboguer en imprimant et en vérifiant le résultat à la main. Voici quelques suggestions pour déboguer de grands ensembles de données:
Réduire l'entrée: Si possible, réduisez la taille du jeu de données. Par exemple, si le programme lit un fichier texte, commencez par les 10 premières lignes ou par le plus petit exemple.
tu peux trouver. Vous pouvez soit éditer les fichiers eux-mêmes, soit (mieux) modifier le programme
il ne lit donc que les n premières lignes.
S'il y a une erreur, vous pouvez réduire n à la plus petite valeur qui manifeste l'erreur, et
augmentez-le ensuite progressivement à mesure que vous trouvez et corrigez les erreurs.
Vérifier les résumés et les types: au lieu d’imprimer et de vérifier l’ensemble du jeu de données, considérez
l’impression des résumés des données: par exemple, le nombre d’articles dans un dictionnaire ou
le total d'une liste de nombres.
Une cause fréquente d’erreurs d’exécution est une valeur qui n’est pas le bon type. Pour le débogage
ce type d'erreur, il suffit souvent d'imprimer le type d'une valeur.
Écrire des auto-vérifications: vous pouvez parfois écrire du code pour rechercher automatiquement les erreurs. Pour
Par exemple, si vous calculez la moyenne d’une liste de nombres, vous pouvez vérifier que
le résultat n'est pas supérieur au plus grand élément de la liste ni inférieur au plus petit.
Cela s'appelle un «contrôle de cohérence», car il détecte les résultats «insensés».
Un autre type de vérification compare les résultats de deux calculs différents pour voir si
ils sont cohérents. Cela s'appelle un «contrôle de cohérence».

112

Chapitre 11. Dictionnaires

Formater la sortie: le formatage de la sortie de débogage peut permettre de repérer plus facilement une erreur. nous
J'ai vu un exemple à la section 6.9. Un autre outil qui pourrait vous être utile est le module pprint, qui fournit une fonction pprint qui affiche les types intégrés dans un format plus lisible par l’humain (pprint signifie «jolie impression»).
Encore une fois, le temps que vous passez à construire un échafaudage peut réduire le temps que vous passez à déboguer.

11.9

Glossaire

mappage: relation dans laquelle chaque élément d'un ensemble correspond à un élément de
un autre ensemble.
dictionnaire: une correspondance entre les clés et leurs valeurs correspondantes.
paire clé-valeur: La représentation du mappage d'une clé à une valeur.
item: dans un dictionnaire, un autre nom pour une paire clé-valeur.
clé: objet qui apparaît dans un dictionnaire en tant que première partie d'une paire clé-valeur.
valeur: objet qui apparaît dans un dictionnaire en tant que deuxième partie d'une paire clé-valeur. C'est
plus spécifique que notre utilisation précédente du mot «valeur».
implémentation: une façon de faire un calcul.
hashtable: l'algorithme utilisé pour implémenter les dictionnaires Python.
fonction de hachage: fonction utilisée par une table de hachage pour calculer l'emplacement d'une clé.
hashable: type ayant une fonction de hachage. Types immuables comme les entiers, les flottants et les chaînes
sont hashable; les types mutables tels que les listes et les dictionnaires ne le sont pas.
lookup: Une opération de dictionnaire qui prend une clé et trouve la valeur correspondante.
recherche inversée: opération de dictionnaire qui prend une valeur et trouve une ou plusieurs clés
carte à elle.
déclaration de levée: une déclaration qui (délibérément) soulève une exception.
singleton: liste (ou autre séquence) avec un seul élément.
graphe d'appel: un diagramme qui montre chaque image créée lors de l'exécution d'un programme,
avec une flèche de chaque appelant à chaque appelé.
Mémo: Une valeur calculée stockée pour éviter des calculs futurs inutiles.
variable globale: une variable définie en dehors d'une fonction. Les variables globales peuvent être consultées
de toute fonction.
déclaration globale: une déclaration qui déclare un nom de variable global.
flag: Une variable booléenne utilisée pour indiquer si une condition est vraie.
déclaration: Une déclaration comme globale qui dit quelque chose à l'interprète à propos d'une variable.

11.10. Des exercices

11h10

113

Des exercices - to be verfied again

Exercice 11.1. Ecrivez une fonction qui lit les mots dans words.txt et les stocke comme clés dans un
dictionnaire. Peu importe les valeurs. Ensuite, vous pouvez utiliser l’opérateur in comme moyen rapide de
vérifie si une chaîne est dans le dictionnaire.
Si vous avez fait l’exercice 10.10, vous pouvez comparer la vitesse de cette implémentation à la liste de l’opérateur
et la recherche de bissection.
Exercice 11.2. Lisez la documentation de la méthode du dictionnaire setdefault et utilisez-la pour écrire un
version plus concise de invert_dict. Solution: http: // thinkpython2. com / code / invert_
dict. py.
Exercice 11.3. Mémoisez la fonction Ackermann de l'exercice 6.2 et voir si la mémoization
permet d'évaluer la fonction avec des arguments plus grands. Indice: non. Solution: http:
// thinkpython2. com / code / mémo ackermann_. py.
Exercice 11.4. Si vous avez fait l’exercice 10.7, vous avez déjà une fonction nommée has_duplicates qui
prend une liste en tant que paramètre et renvoie True si un objet apparaît plusieurs fois dans la liste.
liste.
Utilisez un dictionnaire pour écrire une version plus rapide et plus simple de has_duplicates. Solution: http: //
thinkpython2. com / code / has_ ​​en double. py.
Exercice 11.5. Deux mots sont des "paires tournantes" si vous pouvez faire pivoter l’un d’eux et obtenir l’autre (voir
rotate_word dans l'exercice 8.5).
Ecrivez un programme qui lit une liste de mots et trouve toutes les paires de rotation. Solution: http: //
thinkpython2. com / code / rotation_ paires. py.
Exercice 11.6. Voici un autre Puzzler de Car Talk (http: // www. Cartalk. Com / content /
casse-tête):
Cela a été envoyé par un gars nommé Dan O'Leary. Il est tombé sur une syllabe commune,
mot de cinq lettres récemment qui a la propriété unique suivante. Lorsque vous retirez le
première lettre, les lettres restantes forment un homophone du mot original, c’est un mot
ça sonne exactement pareil. Remplacez la première lettre, c’est-à-dire remettez-la en place et retirez-la.
la deuxième lettre et le résultat est encore un autre homophone du mot original. Et le
La question est: quel est le mot?
Maintenant, je vais vous donner un exemple qui ne fonctionne pas. Regardons les cinq lettres
W-R-A-C-K, vous savez aimer «‘ rayer avec douleur ». Si j’enlève le premier
lettre, il me reste un mot de quatre lettres, "R-A-C-K". Comme dans "Holy cow, did you see the
rack on that buck! It must have been a nine-pointer! ». C’est un homophone parfait. Si vous
remettez le "w" en arrière et supprimez le "r" à la place, vous avez le mot "wack" qui est
un vrai mot, ce n’est tout simplement pas un homophone des deux autres mots.
Mais il y a cependant au moins un mot que Dan et nous connaissons, qui donnera deux
homophones si vous supprimez l'une des deux premières lettres pour en faire deux nouvelles
mots. La question est, quel est le mot?
Vous pouvez utiliser le dictionnaire de l’exercice 11.1 pour vérifier si une chaîne est dans la liste de mots.
Pour vérifier si deux mots sont homophones, vous pouvez utiliser le dictionnaire de prononciation CMU. Vous
peut le télécharger à partir de http: // www. discours. cs. cmu. edu / cgi-bin / cmudict ou de http:
// thinkpython2. com / code / c06d et vous pouvez également télécharger http: // thinkpython2.
com / code / prononcer. py, qui fournit une fonction nommée read_dictionary qui lit le
prononcer dictionnaire et retourne un dictionnaire Python qui mappe de chaque mot à une chaîne qui
décrit sa prononciation principale.

114

Chapitre 11. Dictionnaires

Ecrivez un programme qui liste tous les mots qui résolvent le Puzzler. Solution: http: // thinkpython2.
com / code / homophone. py.# La Pensée Python, Comment raisonner comme un scientiste de l'informatique

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
wiki/ Koch_ snowflake pour des exemples et implémentez votre favori.from os import listdir
from os.path import isfile, join

mypath = '../translated'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    with open(f, 'r', encoding="utf8") as trf:
        with open('newf.md', 'a', encoding="utf8") as mdf:
            mdf.write(trf.read())﻿Chapitre 1
Le chemin de la programmation

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

<page 2> 

Chapitre 1. Le chemin de la programmation

Répétition: Effectuez une action répétée, habituellement avec une certaine variation.

Croyez-le ou non, c'est à peu près tout ce qu'il y a à faire. Chaque programme que vous avez déjà utilisé, quelle que soit la complexité, se compose d'instructions qui ressemblent à peu près à celles-ci. Ainsi, vous pouvez penser à la programmation en tant que processus de rupture d'une tâche complexe en de sous-tâches plus petites et plus petites jusqu'à ce que les sous-tâches soient assez simples pour être exécutées avec une de ces instructions de base.

1.2 Exécuter Python

L'un des défis de commencer avec Python est que vous devrez peut-être installer Python et logiciels relatifs sur votre ordinateur. Si vous connaissez votre système d’exploitation, et surtout si vous êtes à l'aise avec l'interface ligne de commande, vous n'aurez aucun problème pour installer Python. Mais pour les débutants, il peut être douloureux de connaître le système d'administration et la programmation en même temps.

Pour éviter ce problème, je vous recommande de commencer à exécuter Python dans un navigateur. Plus tard, lorsque vous êtes à l'aise avec Python, je ferai des suggestions pour installer Python sur votre ordinateur.

Il existe un certain nombre de pages Web que vous pouvez utiliser pour exécuter Python. Si vous avez déjà un favori, allez-y et utilisez-le. Sinon, je recommande PythonAnywhere. Voyez les instructions sur http://tinyurl.com/thinkpython2e 

Il existe deux versions de Python, appelées Python 2 et Python 3. Elles sont très similaires, donc si vous en apprendrez un, il est facile de passer à l'autre. En fait, il n'y a que quelques différences que vous rencontrerez en tant que débutant. Ce livre est écrit pour Python 3, mais j'ai inclu des notes sur Python 2.

L'interpréteur Python est un programme qui lit et exécute le code Python. En fonction, dépendent sur votre environnement, vous pouvez lancer l'interprète en cliquant sur une icône ou en tapant python sur une ligne de commande. Quand cela commence, vous devriez voir:

Python 3.4.0 (default, Jun 19 2015, 14:20:21)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

Les trois premières lignes contiennent des informations sur l'interprète et le système d'exploitation actuel, donc il pourrait être différent pour vous. Mais vous devez vérifier que le numéro de version, qui est 3.4.0 dans cet exemple, commence par 3, ce qui indique que vous utilisez Python 3. Si cela commence avec 2, vous exécutez (vous l'avez deviné) Python 2.

La dernière ligne est indique que l'interprète est prêt à recevoir le code. Si vous tapez une ligne de code et appuyez sur Entrée (sur le clavier), l'interprète affiche le résultat:

>>> 1 + 1
2

Maintenant, vous êtes prêt à commencer. À partir de là, je suppose que vous savez comment commencer l’interprète de Python et exécuter des lignes de code.

<page 3>

1.3 Le premier programme

Traditionnellement, le premier programme que vous écrivez dans une nouvelle langue s'appelle "Hello, World!" Parce que tout ce qu'il fait, c'est d'afficher les mots "Hello, World!". Dans Python, cela ressemble à ceci:

>>> print('Hello, World!')

Il s'agit d'un exemple d'une déclaration d'impression, bien qu'il n'imprime en réalité rien sur papier. Il affiche un résultat sur l'écran. Dans ce cas, le résultat est les mots

Hello, World!

Les guillemets dans le programme marquent le début et la fin du texte à afficher ; ils n'apparaissent pas dans le résultat.

Les parenthèses indiquent que l'impression est une fonction. Nous aborderons les fonctions du chapitre 3.

Dans Python 2, l'instruction d'impression est légèrement différente; ce n'est pas une fonction, donc les parenthèses, ça ne sert à rien.

>>> print 'Hello, World!'

Cette distinction aura plus de sens bientôt, mais c'est assez pour commencer.

1.4 Opérateurs arithmétiques

Après " Hello, World!", la prochaine étape est l'arithmétique. Python fournit aux opérateurs, qui sont des symboles spéciaux qui représentent des calculs comme addition et multiplication.

Les opérateurs +, -, et * effectuent l'addition, la soustraction et la multiplication, comme suit
exemples:

>>> 40 + 2
42
>>> 43 - 1
42
>>> 6 * 7
42
L'opérateur / exécute la division:
>>> 84/2
42,0

Vous pourriez vous demander pourquoi le résultat est 42.0 au lieu de 42. Je vais vous expliquer dans la prochaine section.

Enfin, l'opérateur ** effectue une exponentiation; c'est-à-dire qu'il soulève un nombre à une puissance:

>>> 6 ** 2 + 6
42

Dans certaines autres langues, ^ est utilisé pour l'exponentiation, mais en Python, c'est un opérateur bit à bit appelé XOR. Si vous n'êtes pas familiarisé avec les opérateurs bit à bit, le résultat vous surprendra:
>>> 6 ^ 2
4
Je ne couvrirai pas les opérateurs bit à bit dans ce livre, mais vous pouvez les lire sur http://wiki.python.org/moin/BitwiseOperators.

<page 4>
 Chapitre 1. Le chemin de la programmation

1.5 Valeurs et types

Une valeur est l'une des choses de base avec laquelle un programme fonctionne, comme une lettre ou un numéro. Certains des valeurs que nous avons vues jusqu'ici sont 2, 42.0, et 'Hello, World!'.

Ces valeurs appartiennent à différents types: 2 est un nombre entier, 42.0 est un float alias nombre décimal et 'Hello, World!' est une chaîne (string en anglais), soi-disant parce que les lettres qu'il contient sont enfilées ensemble.

Si vous ne savez pas quel type de valeur a, l'interprète peut vous dire:
>>> type (2)
<classe 'int'>
>>> type (42.0)
<classe 'float'>
>>> type (' Hello, World!')
<classe 'str'>

Dans ces résultats, le mot «class» est utilisé au sens d'une catégorie; un type est une catégorie de valeurs.

Il n'est pas surprenant que les entiers appartiennent au type int, les chaînes appartiennent à str et les nombres à virgule flottante à float.

Qu'en est-il des valeurs comme '2' et '42 .0 '? Ils ressemblent à des chiffres, mais ils sont en citations comme les strings.
>>> type ('2')
<classe 'str'>
>>> type ('42 .0 ')
<classe 'str'>
Ils sont des strings.

Lorsque vous tapez un grand nombre entier, vous pourriez être tenté d'utiliser des virgules entre les groupes de chiffres, soit 1 000 000. Ce n'est pas un entier juridiquement parlant en Python, mais c'est légal :

>>> 1,000,000
(1, 0, 0)
Ce n'est pas ce à quoi nous nous attendions du tout! Python interprète 1 000 000 comme une séquence d'entiers séparé par des virgules. Nous en apprendrons d’avantage sur ce genre de séquence plus tard.

1.6 Langues formelles et naturelles

Les langues sont les langues que les gens parlent, comme l'anglais, l'espagnol et le français. Ils n'étaient pas conçus par les gens (bien que les gens essayent d'imposer un ordre sur eux); ils évoluent naturellement.

Les langues formelles sont des langages conçus par des personnes pour des applications spécifiques. Par exemple, la notation utilisée par les mathématiciens est un langage formel qui est en particulier bien apte à dénoter les relations entre les nombres et les symboles. Les chimistes utilisent une langue formelle pour représenter la structure moléculaire des atomes. Et, surtout:

Les langages de programmation sont des langages formels conçus pour
exprimer les calculs.

<page 5>
1.6. Langues formelles et naturelles

Les langues formelles ont tendance à avoir des règles de syntaxe strictes qui régissent la structure des déclarations. Par exemple, en mathématiques, la déclaration 3 + 3 = 6 a une syntaxe correcte, mais 3+ = 3 $ 6 ne l’est pas. En chimie H2O est une formule syntaxiquement correcte, mais 2Zz n'est pas.

Les règles de syntaxe comportent deux saveurs, relatives aux tokens et à la structure. Les tokens sont les éléments basiques de la langue, tels que les mots, les chiffres et les éléments chimiques. Un des problèmes avec 3+ = 3 $ 6 est que $ n'est pas un token juridique en mathématiques (du moins à ce que je sais). De même, 2Zz n'est pas légal car il n'y a aucun élément avec l'abréviation Zz.

Le second type de règle de syntaxe concerne la façon dont les tokens sont combinés. L'équation 3 += 3 est illégal car même si + et = sont des tokens légaux, vous ne pouvez pas avoir un après l'autre. De même, dans une formule chimique, l'indice vient après le nom de l'élément, pas avant.

C'est une phr@se anglaise bien $tructurée avec t*kens invalide. Cette phrase valable tokens a, mais structure invalide avec.

Lorsque vous lisez une phrase en anglais ou une déclaration dans une langue officielle, vous devez identifier la structure (bien que dans une langue naturelle, vous faites cela de façon inconsciente). Ce
processus s'appelle parsing (analyse).

Bien que les langages formels et naturels possèdent de nombreuses caractéristiques communs : les token, la structure, et la syntaxe - il y a des différences:

ambiguïté: les langues naturelles sont pleines d'ambiguïté, auxquelles les gens s'occupent en utilisant des indices contextuels et d'autres informations. Les langues officielles sont conçues pour être presque ou totalement sans ambiguïté, ce qui signifie que toute déclaration a exactement un sens, quel que soit le contexte.

redondance: afin de compenser l'ambiguïté et de réduire les malentendus, les langues naturelles utilisent beaucoup de redondance. En conséquence, ils sont souvent détaillés. Les langues formelles sont moins redondantes et plus concises.

littéralité: les langues naturelles sont pleines d'idiome et de métaphore. Si je dis en anglais: "The penny dropped" (litt. le penny est tombé), il n'y a probablement pas de penny et rien n’est tombé (cette idiome signifie que quelqu'un a compris quelque chose après une période de confusion). Les langues formelles signifient exactement ce qu'ils disent. Parce que nous grandissons tous en parlant des langues naturelles, il est parfois difficile de s'adapter à la forme langues. La différence entre langage formel et naturel est comme la différence entre la poésie et la prose, mais plus encore:

Poésie: les mots sont utilisés pour leurs sons aussi bien que pour leur signification, et le poème entier ensemble crée un effet ou une réponse émotionnelle. L'ambiguïté n'est pas seulement souvent mais aussi délibéré.

Prose: le sens littéral des mots est plus important, et la structure contribue davantage au sens. La prose est plus susceptible d'analyse que le poésie, mais toujours ambiguë.

Programmes: la signification d'un programme informatique est sans ambiguïté et littérale, et peut être entièrement compris par l'analyse des tokens et de la structure.

<page 6> 
Chapitre 1. Le chemin de la programmation

Les langues formelles sont plus denses que les langues naturelles, il faut donc plus de temps pour les lire. En outre, la structure est importante, donc il n'est pas toujours préférable de lire de haut en bas, de gauche à droite. Au lieu de cela, apprenez à analyser le programme dans votre tête, identifiant les tokens et l'interprétation de la structure. Enfin, les détails sont importants. De petites erreurs dans l'orthographe et la ponctuation, dont vous pouvez vous en sortir dans des langues naturelles, peut faire une grande différence dans une langue formelle.

1.7 Débogage

Les programmeurs font des erreurs. Pour des raisons capricieuses, les erreurs de programmation sont appelées bugs et le processus de suivi est appelé débogage.
La programmation, et en particulier le débogage, soulève parfois de fortes émotions. Si vous êtes en face d’un bug difficile, vous pouvez vous sentir en colère, découragé ou embarrassé.
Il existe des preuves que les gens répondent naturellement aux ordinateurs comme s'ils étaient des gens. Quand ils fonctionnent bien, on les considère comme des coéquipiers, et quand ils sont obstinés ou grossiers, nous répondons à eux de la même manière que nous répondons à des personnes grossières et obstinées (Reeves and Nass, The Media Equation: How People Treat Computers, Television, and New Media Like Real People
and Places) .

Préparer à ces réactions pourrait vous aider à les traiter. Une approche consiste à penser à l'ordinateur en tant qu'employé avec certaines forces, comme la vitesse et la précision, et en particulier les faiblesses, comme le manque d'empathie et l'incapacité de saisir l’image en gros.

Votre travail consiste à être un bon gestionnaire: trouver des moyens de tirer parti des atouts et atténuer les faiblesses. Et trouver des façons d'utiliser vos émotions pour s'engager dans le problème, sans laisser vos réactions interférer avec votre capacité à travailler efficacement.

Apprendre à déboguer peut être frustrant, mais c'est une compétence précieuse qui est utile pour de nombreuses activités au-delà de la programmation. À la fin de chaque chapitre, il y a une section, comme celle-ci, avec
mes suggestions de débogage. J'espère qu'ils vous seront utiles!

1.8 Glossaire

résolution de problèmes / problem-solving: le processus de formulation d'un problème, la recherche d'une solution et l'exprimer.

Langage haut niveau / high-level language: un langage de programmation comme Python conçu pour être facile pour les humains à lire et à écrire.

langage de bas niveau / low-level language: un langage de programmation conçu pour être facile pour un ordinateur de parcourir; également appelé "language machine" ou "language assembly".

portabilité: une propriété d'un programme qui peut fonctionner sur plus d'un type d'ordinateur.

interprète: un programme qui lit un autre programme et l'exécute

prompt: caractères affichés par l'interprète pour indiquer qu'il est prêt à prendre une entrée de l'utilisateur.

programme: un ensemble d'instructions qui spécifient un calcul.
1.9. Exercices 
<page 7>

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

1.9 Exercices

Exercice 1.1. 
C'est une bonne idée de lire ce livre devant un ordinateur afin que vous puissiez essayer les exemples que vous allez lire.

Chaque fois que vous expérimentez avec une nouvelle fonctionnalité, vous devriez essayer de faire des erreurs. Par exemple, dans le programme «Hello World!», qu'arrive-t-il si vous laissez une des guillemets? Et qu'est-ce qui se passerait si vous quittez les deux? Que se passe-t-il si vous écrivez une mauvaise impression? Ce genre d'expérience vous aide à vous souvenir de ce que vous lisez. Cela vous aide également lorsque vous programmez, parce que vous comprenez ce que signifient les messages d'erreur. Il est préférable de faire des fautes maintenant et que plus tard et accidentellement.

1. Dans un print staement , que se passe-t-il si vous excluez l'une des parenthèses, ou les deux?

2. Si vous essayez d'imprimer une chaîne, que se passe-t-il si vous laissez une des guillemets, ou les deux?

3. Vous pouvez utiliser un signe moins pour créer un nombre négatif comme -2. Que se passe-t-il si vous mettez un + avant un nombre? Qu'en est-il de 2 ++ 2?

<page 8>
 Chapitre 1. Le chemin de la programmation

4. En notation mathématique, les zéros avancés sont corrects, comme en 02. Que se passe-t-il si vous essayez cela dans Python?

5. Que se passe-t-il si vous avez deux valeurs sans opérateur entre elles?

Exercice 1.2. Démarrez l'interpréteur Python et utilisez-le comme calculatrice.

1. Combien de secondes existe-t-il en 42 minutes 42 secondes?
2. Combien y a-t-il de miles en 10 kilomètres? Astuce: il y a 1,61 kilomètre dans un mile.
3. Si vous exécutez une course de 10 kilomètres en 42 minutes 42 secondes, quel est votre rythme moyen (temps par mile en minutes et secondes)? Quelle est votre vitesse moyenne en miles par heure?

