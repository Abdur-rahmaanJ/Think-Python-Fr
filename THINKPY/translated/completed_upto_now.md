
# La Pensée Python, Comment raisonner comme un scientiste de l'informatique

traduction du livre: 

### Think Python, How To Think Like A Computer Scientist 

#### d'Allan Downey

- par Abdur-Rahmaan Janhangeer de l'Ile Maurice 

<hr>

# Indexe

- [Chapitre 1: le chemin de la programmation](#ch1)
- [Chapitre 2: variables, expressions et déclarations](#ch2)
- [Chapitre 3: les fonctions](#ch3)
- [Chapitre 4: conception d'interface](#ch4)
- [Chapitre 5: conditions et récursivité](#ch5)
- [Chapitre 6: fonctions fructueuses](#ch6)
- [Chapitre 7: itération](#ch7)
- [Chapitre 8: strings ](#ch8)
- [Chapitre 9: jeu de mots ](#ch9)

<hr>

# Chapitre 1<a name="ch1"></a>

## Le chemin de la programmation
<br><br>
Le but de ce livre est de vous apprendre à penser comme un informaticien. Cette façon de penser combine certaines des meilleures caractéristiques des maths, de l'ingénierie et des sciences naturelles.
Comme les mathématiciens, les informaticiens utilisent des langages formels pour désigner des idées (en particulier les calculs). Comme les ingénieurs, ils conçoivent des choses, assemblent des composants dans des systèmes et évaluent les compromis entre les alternatives. Comme les scientifiques, ils observent le comportement des systèmes complexes, forment des hypothèses et testent des prédictions.

La compétence la plus importante pour un informaticien est la résolution de problèmes. La résolution des problèmes signifie la capacité de formuler des problèmes, réfléchir de manière créative aux solutions et exprimer une solution claire et précise. Dans l'affirmative, le processus d'apprentissage au programmation est une excellente occasion d’affiner ses compétences en matière de résolution de problèmes. C'est pourquoi ce chapitre s'appelle,
"Le chemin de la programmation".

À un niveau, vous apprendrez à programmer, une compétence utile en soi. Sur un autre niveau, vous utiliserez la programmation comme un moyen d'atteindre une fin. À mesure que nous progressons, cette fin deviendra plus claire.

### 1.1 Qu'est-ce qu'un programme?

Un programme est une séquence d'instructions qui spécifie comment effectuer un calcul. Le calcul peut être quelque chose de mathématique, comme la résolution d'un système d'équations ou trouver les racines d'un polynôme, mais il peut également s'agir d'un calcul symbolique, comme la recherche, remplacer du texte dans un document ou quelque chose de graphique, comme le traitement d'une image ou jouer une vidéo.

Les détails sont différents dépendant des langues, mais quelques instructions de base apparaissent dans la plupart des langues:

- Entrée: Obtenez des données du clavier, d'un fichier, du réseau ou d'un autre appareil.

- Sortie: afficher les données sur l'écran, l'enregistrer dans un fichier, envoie sur réseau, etc.

- Maths: effectuez des opérations mathématiques de base comme addition et multiplication.

- Exécution conditionnelle: vérifier certaines conditions et exécuter le code approprié.

- Répétition: Effectuez une action répétée, habituellement avec une certaine variation.

Croyez-le ou non, c'est à peu près tout ce qu'il y a à faire. Chaque programme que vous avez déjà utilisé, quelle que soit la complexité, se compose d'instructions qui ressemblent à peu près à celles-ci. Ainsi, vous pouvez penser à la programmation en tant que processus de rupture d'une tâche complexe en de sous-tâches plus petites et plus petites jusqu'à ce que les sous-tâches soient assez simples pour être exécutées avec une de ces instructions de base.

### 1.2 Exécuter Python

L'un des défis de commencer avec Python est que vous devrez peut-être installer Python et logiciels relatifs sur votre ordinateur. Si vous connaissez votre système d’exploitation, et surtout si vous êtes à l'aise avec l'interface de ligne de commande, vous n'aurez aucun problème pour installer Python. Mais pour les débutants, il peut être douloureux d'apprendre l'administration du système et la programmation en même temps.

Pour éviter ce problème, je vous recommande de commencer à exécuter Python dans un navigateur. Plus tard, lorsque vous êtes à l'aise avec Python, je ferai des suggestions pour installer Python sur votre ordinateur.

Il existe un certain nombre de pages Web que vous pouvez utiliser pour exécuter Python. Si vous avez déjà un favori, allez-y et utilisez-le. Sinon, je recommande PythonAnywhere. Voyez les instructions sur 
[http://tinyurl.com/thinkpython2e](http://tinyurl.com/thinkpython2e)

Il existe deux versions de Python, appelées Python 2 et Python 3. Elles sont très similaires, donc si vous en apprendrez un, il est facile de passer à l'autre. En fait, il n'y a que quelques différences que vous rencontrerez en tant que débutant. Ce livre est écrit pour Python 3, mais j'ai inclu des notes sur Python 2.

**L'interpréteur** Python est un programme qui lit et exécute le code Python. En fonction de votre environnement, vous pouvez lancer l'interprète en cliquant sur une icône ou en tapant python sur une ligne de commande. Quand cela commence, vous devriez voir:

```python
Python 3.4.0 (default, Jun 19 2015, 14:20:21)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Les trois premières lignes contiennent des informations sur l'interprète et le système d'exploitation actuel, donc il pourrait être différent pour vous. Mais vous devez vérifier que le numéro de version, qui est 3.4.0 dans cet exemple, commence par 3, ce qui indique que vous utilisez Python 3. Si cela commence avec 2, vous exécutez (vous l'avez deviné) Python 2.

La dernière ligne indique que l'interprète est prêt à recevoir le code. Si vous tapez une ligne de code et appuyez sur Entrée (sur le clavier), l'interprète affiche le résultat:

```python
>>> 1 + 1
2
```

Maintenant, vous êtes prêt à commencer. À partir de là, je suppose que vous savez comment commencer l’interprète de Python et exécuter des lignes de code.

### 1.3 Le premier programme

Traditionnellement, le premier programme que vous écrivez dans une nouvelle langue s'appelle "Hello, World!" Parce que tout ce qu'il fait, c'est d'afficher les mots "Hello, World!". Dans Python, cela ressemble à ceci:

```python
>>> print('Hello, World!')
```

Il s'agit d'un exemple d'une déclaration d'impression, bien qu'il n'imprime en réalité rien sur papier. Il affiche un résultat sur l'écran. Dans ce cas, le résultat est les mots

```
Hello, World!
```

Les guillemets dans le programme marquent le début et la fin du texte à afficher ; ils n'apparaissent pas dans le résultat.

Les parenthèses indiquent que l'impression est une fonction. Nous aborderons les fonctions du [chapitre 3](#ch3).

Dans Python 2, l'instruction d'impression est légèrement différente; ce n'est pas une fonction, donc les parenthèses, ça ne sert à rien.

```python
>>> print 'Hello, World!'
```

Cette distinction aura plus de sens bientôt, mais c'est assez pour commencer.

### 1.4 Opérateurs arithmétiques

Après ```" Hello, World!"```, la prochaine étape est l'arithmétique. Python fournit aux opérateurs, qui sont des symboles spéciaux qui représentent des calculs comme addition et multiplication.

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

Dans certaines autres langues, ^ est utilisé pour l'exponentiation, mais en Python, c'est un opérateur bit appelé XOR. Si vous n'êtes pas familiarisé avec les opérateurs bit, le résultat vous surprendra:

```python
>>> 6 ^ 2
4
```

Je ne couvrirai pas les opérateurs bit à bit dans ce livre, mais vous pouvez les lire sur 
[http://wiki.python.org/moin/BitwiseOperators](http://wiki.python.org/moin/BitwiseOperators).

### 1.5 Valeurs et types

Une valeur est l'une des choses de base avec laquelle un programme fonctionne, comme une lettre ou un numéro. Certains des valeurs que nous avons vues jusqu'ici sont ```2```, ```42.0```, et ```'Hello, World!'```.

Ces valeurs appartiennent à différents types: ```2``` est un nombre entier, ```42.0``` est un float alias nombre décimal et ```'Hello, World!'``` est une chaîne de charactères (string en anglais), soi-disant parce que les lettres qu'il contient sont enfilées ensemble.

Si vous ne savez pas de quel type est une valeur, l'interprète peut vous dire:

```python
>>> type (2)
<classe 'int'>
>>> type (42.0)
<classe 'float'>
>>> type (' Hello, World!')
<classe 'str'>
```

Dans ces résultats, le mot ```«class»``` est utilisé au sens d'une catégorie; un type est une catégorie de valeurs.

Il n'est pas surprenant que les entiers appartiennent au type ```int```, les chaînes appartiennent à ```str``` et les nombres à virgule flottante à ```float```.

Qu'en est-il des valeurs comme ```'2'``` et ```'42 .0 '```? Ils ressemblent à des chiffres, mais ils sont en citations comme les strings.

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
Ce n'est pas ce à quoi nous nous attendions du tout! Python interprète 1,000,000 comme une séquence d'entiers séparé par des virgules. Nous en apprendrons d’avantage sur ce genre de séquence plus tard.

### 1.6 Langues formelles et naturelles

Les langues sont les langues que les gens parlent, comme l'anglais, l'espagnol et le français. Ils n'étaient pas conçus par les gens (bien que les gens essayent d'imposer un ordre sur eux); ils évoluent naturellement.

Les langues formelles sont des langages conçus par des personnes pour des applications spécifiques. Par exemple, la notation utilisée par les mathématiciens est un langage formel qui est en particulier bien apte à dénoter les relations entre les nombres et les symboles. Les chimistes utilisent une langue formelle pour représenter la structure moléculaire des atomes. Et, surtout:

> **Les langages de programmation sont des langages formels conçus pour exprimer les calculs.**

Les langues formelles ont tendance à avoir des règles de syntaxe strictes qui régissent la structure des déclarations. Par exemple, en mathématiques, la déclaration ```3 + 3 = 6``` a une syntaxe correcte, mais ```3+ = 3 $ 6``` ne l’est pas. En chimie H<sub>2</sub>O est une formule syntaxiquement correcte, mais <sub>2</sub>Zz ne l'est pas.

Les règles de syntaxe comportent deux saveurs, relatives aux tokens et à la structure. Les tokens sont les éléments basiques de la langue, tels que les mots, les chiffres et les éléments chimiques. Un des problèmes avec ``3+ = 3 $ 6`` est que ```$``` n'est pas un token juridique en mathématiques (du moins à ce que je sais). De même, <sub>2</sub>Zz n'est pas légal car il n'y a aucun élément avec l'abréviation Zz.

Le second type de règle de syntaxe concerne la façon dont les tokens sont combinés. L'équation ```3 += 3 est illégal``` car même si + et = sont des tokens légaux, vous ne pouvez pas avoir un après l'autre. De même, dans une formule chimique, l'indice vient après le nom de l'élément, pas avant.

Ceci une phr@se bien $tructurée avec t * kens invalide. Cette phrase valable tokens a, mais structure invalide avec.

Lorsque vous lisez une phrase ou une déclaration dans une langue officielle, vous devez identifier la structure (bien que dans une langue naturelle, vous faites cela de façon inconsciente). Ce processus s'appelle parsing (analyse).

Bien que les langages formels et naturels possèdent de nombreuses caractéristiques communs : les token, la structure, et la syntaxe - il y a des différences:

- **ambiguïté:** les langues naturelles sont pleines d'ambiguïté, auxquelles les gens s'occupent en utilisant des indices contextuels et d'autres informations. Les langues officielles sont conçues pour être presque ou totalement sans ambiguïté, ce qui signifie que toute déclaration a exactement un sens, quel que soit le contexte.

- **redondance:** afin de compenser l'ambiguïté et de réduire les malentendus, les langues naturelles utilisent beaucoup de redondance. En conséquence, ils sont souvent détaillés. Les langues formelles sont moins redondantes et plus concises.

- **littéralité:** les langues naturelles sont pleines d'idiome et de métaphore. Si je dis en anglais: "The penny dropped" (litt. le penny est tombé), il n'y a probablement pas de penny et rien n’est tombé (cette idiome signifie que quelqu'un a compris quelque chose après une période de confusion). Les langues formelles signifient exactement ce qu'ils disent. Parce que nous grandissons tous en parlant des langues naturelles, il est parfois difficile de s'adapter à la forme langues. La différence entre langage formel et naturel est comme la différence entre la poésie et la prose, mais plus encore:

- **Poésie:** les mots sont utilisés pour leurs sons aussi bien que pour leur signification, et le poème entier ensemble crée un effet ou une réponse émotionnelle. L'ambiguïté n'est pas seulement souvent mais aussi délibéré.

- **Prose:** le sens littéral des mots est plus important, et la structure contribue davantage au sens. La prose est plus susceptible d'analyse que le poésie, mais toujours ambiguë.

- **Programmes:** la signification d'un programme informatique est sans ambiguïté et littérale, et peut être entièrement compris par l'analyse des tokens et de la structure.


Les langues formelles sont plus denses que les langues naturelles, il faut donc plus de temps pour les lire. En outre, la structure est importante, donc il n'est pas toujours préférable de lire de haut en bas, de gauche à droite. Au lieu de cela, apprenez à analyser le programme dans votre tête, identifiant les tokens et l'interprétation de la structure. Enfin, les détails sont importants. De petites erreurs dans l'orthographe et la ponctuation, dont vous pouvez vous en sortir dans des langues naturelles, peut faire une grande différence dans une langue formelle.

### 1.7 Débogage

Les programmeurs font des erreurs. Pour des raisons capricieuses, les erreurs de programmation sont appelées bugs et le processus de suivi est appelé débogage.
La programmation, et en particulier le débogage, soulève parfois de fortes émotions. Si vous êtes en face d’un bug difficile, vous pouvez vous sentir en colère, découragé ou embarrassé.

Il existe des preuves que les gens répondent naturellement aux ordinateurs comme s'ils étaient des gens. Quand ils fonctionnent bien, on les considère comme des coéquipiers, et quand ils sont obstinés ou grossiers, nous répondons à eux de la même manière que nous répondons à des personnes grossières et obstinées (Reeves and Nass, _The Media Equation: How People Treat Computers, Television, and New Media Like Real People
and Places_) .

Se préparer à ces réactions pourrait vous aider à les traiter. Une approche consiste à penser à l'ordinateur en tant qu'employé avec certaines forces, comme la vitesse et la précision, et en particulier les faiblesses, comme le manque d'empathie et l'incapacité de saisir l’image en gros.

Votre travail consiste à être un bon gestionnaire: trouver des moyens de tirer parti des atouts et atténuer les faiblesses. Et trouver des façons d'utiliser vos émotions pour s'engager dans le problème, sans laisser vos réactions interférer avec votre capacité à travailler efficacement.

Apprendre à déboguer peut être frustrant, mais c'est une compétence précieuse qui est utile pour de nombreuses activités au-delà de la programmation. À la fin de chaque chapitre, il y a une section, comme celle-ci, avec mes suggestions de débogage. J'espère qu'ils vous seront utiles!

### 1.8 Glossaire

- **résolution de problèmes / problem-solving:** le processus de formulation d'un problème, la recherche d'une solution et l'exprimer.

- **langage haut niveau / high-level language:** un langage de programmation comme Python conçu pour être facile pour les humains à lire et à écrire.

- **langage de bas niveau / low-level language:** un langage de programmation conçu pour être facile pour un ordinateur de parcourir; également appelé "language machine" ou "langage assembly".

- **portabilité:** une propriété d'un programme qui peut fonctionner sur plus d'un type d'ordinateur.

- **interprète:** un programme qui lit un autre programme et l'exécute

- **prompt:** caractères affichés par l'interprète pour indiquer qu'il est prêt à prendre une entrée de l'utilisateur.

- **programme:** un ensemble d'instructions qui spécifient un calcul.

- **print statement:** une instruction qui amène l'interpréteur Python à afficher une valeur sur l'écran.

- **opérateur:** un symbole spécial qui représente un calcul simple comme : addition, multiplication ou la concaténation de chaîne de caractères .

- **valeur:** une des unités de base de données, comme un nombre ou une chaîne, qu'un programme manipule.

- **type:** une catégorie de valeurs. Les types que nous avons vus jusqu'ici sont des entiers (type int), les nombres flottant (type float) et les chaînes (type str).

- **int:** un type qui représente des nombres entiers.

- **float:** un type qui représente des nombres décimaux.

- **string:** un type qui représente des séquences de caractères.
Langue naturelle: l'une des langues que les gens parlent et qui évolue naturellement.

- **langage formel:** l'une des langues que les gens ont conçues à des fins spécifiques, tels que la représentation d'idées mathématiques ou de programmes informatiques; toute les langues de programmation sont des langues officielles.

- **token:** l'un des éléments de base de la structure syntaxique d'un programme, analogue à un mot dans une langue naturelle.

- **syntax:** les règles qui régissent la structure d'un programme.

- **parsing / analyse:** examiner un programme et analyser la structure syntaxique.

- **bug / bogue:** une erreur dans un programme.

- **débogage:** processus de recherche et de correction de bogues.

### 1.9 Exercices

**Exercice 1**

_C'est une bonne idée de lire ce livre devant un ordinateur afin que vous puissiez essayer les exemples que vous allez lire._

_Chaque fois que vous expérimentez avec une nouvelle fonctionnalité, vous devriez essayer de faire des erreurs. Par exemple, dans le programme «Hello World!», qu'arrive-t-il si vous laissez une des guillemets? Et qu'est-ce qui se passerait si vous quittez les deux? Que se passe-t-il si vous écrivez une mauvaise impression? Ce genre d'expérience vous aide à vous souvenir de ce que vous lisez. Cela vous aide également lorsque vous programmez, parce que vous comprenez ce que signifient les messages d'erreur. Il est préférable de faire des fautes maintenant et que plus tard et accidentellement._

1. Dans un print statement , que se passe-t-il si vous excluez l'une des parenthèses, ou les deux?

2. Si vous essayez d'imprimer une chaîne, que se passe-t-il si vous laissez une des guillemets, ou les deux?

3. Vous pouvez utiliser un signe moins pour créer un nombre négatif comme -2. Que se passe-t-il si vous mettez un + avant un nombre? Qu'en est-il de 2 ++ 2?

4. En notation mathématique, les zéros avancés sont corrects, comme en 02. Que se passe-t-il si vous essayez cela dans Python?

5. Que se passe-t-il si vous avez deux valeurs sans opérateur entre elles?

**Exercice 2**

_Démarrez l'interpréteur Python et utilisez-le comme calculatrice._

1. Combien de secondes existe-t-il en 42 minutes 42 secondes?

2. Combien y a-t-il de miles en 10 kilomètres? Astuce: il y a 1.61 kilomètre dans un mile.

3. Si vous exécutez une course de 10 kilomètres en 42 minutes 42 secondes, quel est votre rythme moyen (temps par mile en minutes et secondes)? Quelle est votre vitesse moyenne en miles par heure?

# Chapitre 2 <a name="ch2"></a>

## Variables, expressions et déclarations
<br><br>
### 2.1 L'affectation

Une **affectation** crée une nouvelle variable et lui donne une valeur

```python
>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.141592653589793
```

Cet exemple fait trois affectations. Le premier attribue une chaîne à une nouvelle variable appelée message; la seconde donne l'entier 17 à n; le troisième attribue la valeur (approximative) de π à pi.

Une manière courante de représenter des variables sur du papier consiste à écrire le nom avec une flèche pointant vers sa valeur. Ce type de figure est appelé diagramme d’état car il indique l’état de chacune des variables (considérez-le comme l’état d’esprit de la variable). La figure 2.1 montre le résultat de l'exemple précédent.

![alt text](assets/tp2.1.png "2.1")

### 2.2 Nom de variables

Les programmeurs choisissent généralement des noms significatifs pour leurs variables - ils documentent l'utilisation de la variable.

Les noms de variables peuvent être aussi longs que vous le souhaitez. Ils peuvent contenir des lettres et des chiffres, mais ils ne peuvent pas commencer par un chiffre. Il est légal d'utiliser des lettres majuscules, mais il est conventionnel de n'utiliser que des minuscules pour les noms de variables.

Le caractère de soulignement _ peut apparaître dans un nom. Il est souvent utilisé dans les noms comportant plusieurs mots, tels que ```your_name``` ou ```airspeed_of_unladen_swallow``` .

Si vous attribuez un nom illégal à une variable, vous obtenez une erreur de syntaxe:

```python
>>> 76trombones = 'grand défilé'
SyntaxError: invalid syntax
>>> more@ = 1000000
SyntaxError: invalid syntax
>>> class = 'Zymurgie théorique avancée'
SyntaxError: invalid syntax
```
```76trombones``` est illégal car il commence par un nombre. ```more@``` est illégal car il contient un caractère illégal, @. Mais quel est le problème avec ```class```?

Il s’avère que ```class``` est l’un des mots clés de Python. L'interprète utilise des mots-clés pour reconnaître la structure du programme et ne peut pas être utilisé comme nom de variable.

Python 3 a ces mots-clés:

```python
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```
Vous n'êtes pas obligé de mémoriser cette liste. Dans la plupart des environnements de développement, les mots-clés sont affichés dans une couleur différente. si vous essayez d’en utiliser un comme nom de variable, vous le saurez.

#### 2.3 Expression et déclarations

Une expression est une combinaison de valeurs, de variables et d'opérateurs. Une valeur en elle-même est considérée comme une expression, de même qu'une variable. Par conséquent ceux-là sont des expressions juridiques:
```python
>>> 42
42
>>> n
17
>>> n + 25
42
```
Lorsque vous tapez une expression au prompt, l'interpréteur l'évalue, ce qui signifie qu'il trouve la valeur de l'expression. Dans cet exemple, ```n``` a la valeur 17 et ```n + 25``` a la valeur 42.

Une instruction est une unité de code qui a un effet, comme créer une variable ou afficher une valeur.

```python
>>> n = 17
>>> imprimer (n)
```
La première ligne est une instruction d’affectation qui donne une valeur à ```n```. La deuxième ligne est une instruction print qui affiche la valeur de ```n```.

Lorsque vous tapez une instruction, l'interprète l'exécute, ce qui signifie qu'il fait tout ce que dit l'instruction. En général, les déclarations n’ont pas de valeurs.

### 2.4 Mode script

Jusqu'à présent, nous avons exécuté Python en mode interactif, ce qui signifie que vous interagissez directement avec l'interpréteur. Le mode interactif est un bon moyen de commencer, mais si vous travaillez avec plus de quelques lignes de code, il peut être maladroit.

L'alternative consiste à enregistrer le code dans un fichier appelé script, puis à exécuter l'interpréteur en mode script pour exécuter le script. Par convention, les scripts Python ont des noms qui se terminent par .py.

Si vous savez créer et exécuter un script sur votre ordinateur, vous êtes prêt. Sinon, je recommande d'utiliser PythonAnywhere à nouveau. J'ai posté des instructions pour l'exécution en mode script à l'adresse [http://tinyurl.com/thinkpython2e](http://tinyurl.com/thinkpython2e).

Comme Python fournit les deux modes, vous pouvez tester des bouts de code en mode interactif avant de les insérer dans un script. Mais il existe des différences entre le mode interactif et le mode script qui peuvent prêter à confusion.

Par exemple, si vous utilisez Python comme calculatrice, vous pouvez taper
```python
>>> miles = 26,2
>>> milles * 1,61
42.182
```
La première ligne attribue une valeur aux miles, mais elle n’a aucun effet visible. La deuxième ligne est une expression, donc l'interprète l'évalue et affiche le résultat. Il s'avère qu'un marathon est d'environ 42 kilomètres.

Mais si vous tapez le même code dans un script et que vous l'exécutez, vous n'obtenez aucune sortie. En mode script, une expression, par elle-même, n'a aucun effet visible. Python évalue réellement l'expression, mais il n'affiche pas la valeur sauf si vous lui indiquez:
```python
miles = 26,2
print(miles * 1,61)
```
Ce comportement peut être déroutant au début.

Un script contient généralement une séquence d'instructions. S'il existe plusieurs instructions, les résultats s'affichent les uns après les autres au fur et à mesure de leur exécution.

Par exemple, le script

```python
print(1)
x = 2
print(x)
```
produit la sortie
```
1
2
```
L'instruction d'affectation ne produit aucune sortie.

Pour vérifier votre compréhension, tapez les instructions suivantes dans l'interpréteur Python et voyez ce qu'elles font:
```python
5
x = 5
x + 1
```
Maintenant, mettez les mêmes instructions dans un script et exécutez-le. Quelle est la sortie? Modifiez le script en transformant chaque expression en une instruction d'impression, puis réexécutez-la.

### 2.5 Ordre des opérations

Lorsqu'une expression contient plusieurs opérateurs, l'ordre d'évaluation dépend de l'ordre des opérations. Pour les opérateurs mathématiques, Python respecte les conventions mathématiques. L'acronyme **PEMDAS** est un moyen utile de mémoriser les règles:

- Les **P**arenthèses ont la priorité la plus élevée et peuvent être utilisées pour forcer l’évaluation d’une expression dans l’ordre que vous souhaitez. Comme les expressions entre parenthèses sont évaluées en premier, ```2 * (3-1)``` est égal à 4 et ```(1 + 1) ** (5-2)``` est égal à 8. Vous pouvez également utiliser des parenthèses pour faciliter la lecture d’une expression, comme dans ```( minute * 100) / 60```, même si cela ne change pas le résultat.

- L'**E**xponentiation a la priorité suivante, donc ```1 + 2 ** 3``` est égal à 9 et non 27 et ```2 * 3 ** 2``` à 18 et non 36.

- La **M**ultiplication et la **D**ivision ont une priorité plus élevée que l'addition et la soustraction. Donc, ```2 * 3-1``` correspond à 5, pas 4, et ```6 + 4/2``` à 8, pas 5.

- Les opérateurs avec la même priorité sont évalués de gauche à droite (sauf l'exponentiation). Ainsi, dans l'expression ```degrees / 2 * pi```, la division se produit en premier et le résultat est multiplié par pi. Pour diviser par 2 π, vous pouvez utiliser des parenthèses ou écrire ```degrees / 2 / pi```.

Je ne travaille pas très dur pour me souvenir de la préséance des opérateurs. Si je ne peux pas dire en regardant l'expression, j'utilise des parenthèses pour la rendre évidente.

### 2.6 Opérations sur les chaînes

En général, vous ne pouvez pas effectuer d’opérations mathématiques sur des chaînes, même si elles ressemblent à des nombres, les opérations suivantes sont donc illégales:

```
'2' - '1' 
'oeufs' / 'facile' 
'troisième' * 'un charme'
```

Mais il y a deux exceptions, + et * .

L'opérateur + effectue la concaténation de chaînes, ce qui signifie qu'il joint les chaînes en les liant de bout en bout. Par exemple:
```python
>>> first = 'throat'
>>> second = 'warbler'
>>> first + second
throatwarbler
```

L'opérateur * travaille également sur les chaînes; il effectue la répétition. Par exemple, ```"Spam" * 3``` est ```"SpamSpamSpam"```. Si l'une des valeurs est une chaîne, l'autre doit être un entier.

Cette utilisation de + et * est logique par analogie avec l'addition et la multiplication. Tout comme ```4 * 3``` équivaut à ```4 + 4 + 4```, nous nous attendons à ce que ```'Spam' * 3``` soit identique à ```'Spam' + 'Spam' + 'Spam'```, et c'est le cas. D'autre part, il existe une différence significative entre la concaténation et la répétition de chaînes et l'addition et la multiplication d'entiers. Pouvez-vous penser à une propriété dont l'addition a que lq concaténation n'ait pas?

### 2.7 Commentaires

À mesure que les programmes deviennent plus grands et plus compliqués, ils deviennent plus difficiles à lire. Les langages formels sont denses et il est souvent difficile de regarder un morceau de code et de comprendre ce qu'il fait ou pourquoi.

Pour cette raison, il est judicieux d’ajouter des notes à vos programmes pour expliquer en langage naturel ce qu’il fait. Ces notes s'appellent des commentaires et commencent par le symbole ```#```:

```python
# calcule le pourcentage de l'heure écoulée
pourcentage = (minute * 100) / 60
```

Dans ce cas, le commentaire apparaît sur une ligne à part. Vous pouvez également mettre des commentaires à la fin d'une ligne:

```python
pourcentage = (minute * 100) / 60 # pourcentage d'une heure
```
Tout ce qui va du ```#``` à la fin de la ligne est ignoré - cela n’a aucun effet sur l’exécution du programme.

Les commentaires sont plus utiles lorsqu'ils documentent des caractéristiques non évidentes du code. Il est raisonnable de supposer que le lecteur peut comprendre ce que fait le code; il est plus utile d'expliquer pourquoi.

Ce commentaire est redondant avec le code et inutile:

```python
v = 5 # assigner 5 à v
```

Ce commentaire contient des informations utiles qui ne figurent pas dans le code:

```python
v = 5 # vitesse en mètres / seconde.
```
De bons noms de variables peuvent réduire le besoin de commentaires, mais des noms longs peuvent rendre les expressions complexes difficiles à lire, ce qui crée un compromis.

### 2.8 Débogage

Trois types d’erreur peuvent se produire dans un programme: les erreurs de syntaxe, les erreurs d’exécution et les erreurs sémantiques. Il est utile de les distinguer afin de les localiser plus rapidement.

- **Erreur de syntaxe:** La «syntaxe» fait référence à la structure d'un programme et aux règles relatives à cette structure. Par exemple, les parenthèses doivent être appariées, donc ```(1 + 2)``` est légal, mais ```8)``` est une erreur de syntaxe.
S'il y a une erreur de syntaxe dans votre programme, Python affiche un message d'erreur et se ferme. Vous ne pourrez pas exécuter le programme. Pendant les premières semaines de votre carrière en programmation, vous passerez peut-être beaucoup de temps à rechercher les erreurs de syntaxe. Au fur et à mesure que vous gagnerez de l'expérience, vous ferez moins d'erreurs et les trouverez plus rapidement.

- **Erreur d'exécution:** Le deuxième type d'erreur est une erreur d'exécution, ainsi appelée car l'erreur n'apparaît pas avant que le programme n'ait commencé à s'exécuter. Ces erreurs sont également appelées exceptions car elles indiquent généralement qu'un événement exceptionnel (et un incident grave) s'est produit.
Les erreurs d'exécution sont rares dans les programmes simples que vous verrez dans les premiers chapitres, il faudra donc peut-être un peu de temps avant d'en rencontrer un.

- **Erreur sémantique:** Le troisième type d'erreur est «sémantique», ce qui signifie lié au sens. S'il y a une erreur sémantique dans votre programme, celui-ci s'exécutera sans générer de message d'erreur, mais cela ne fonctionnera pas correctement. Cela fera autre chose. Plus précisément, il fera ce que vous lui avez dit de faire.
Identifier les erreurs sémantiques peut être délicat, car cela nécessite de travailler en arrière en examinant les résultats du programme et en essayant de comprendre ce qu'il fait.

### 2.9 Glossaire

- **variable:** Un nom qui fait référence à une valeur.

- **affectation:** Une déclaration qui assigne une valeur à une variable.

- **diagramme d'état:** Représentation graphique d'un ensemble de variables et des valeurs auxquelles elles se rapportent.

- **mot-clé:** Mot réservé utilisé pour analyser un programme. vous ne pouvez pas utiliser de mots-clés tels que if, def et while comme noms de variable.

- **opérande:** Une des valeurs sur lesquelles opère un opérateur.

- **expression:** Combinaison de variables, d'opérateurs et de valeurs représentant un seul résultat.

- **évaluer:** Simplifier une expression en effectuant les opérations afin de générer une valeur unique.

- **déclaration:** Une section de code qui représente une commande ou une action. Jusqu'à présent, les déclarations que nous avons vues sont des assignations et des déclarations imprimées.

- **exécuter:** Pour exécuter une déclaration et faire ce qu'elle dit.

- **mode interactif:** Une façon d'utiliser l'interpréteur Python en tapant du code à l'invite.

- **mode script:** Une façon d'utiliser l'interpréteur Python pour lire le code d'un script et l'exécuter.

- **scénario:** Un programme stocké dans un fichier.

- **ordre des opérations:** Règles régissant l'ordre dans lequel les expressions impliquant plusieurs opérateurs et opérandes sont évaluées.

- **enchaîner:** Pour joindre deux opérandes de bout en bout.

- **commentaire:** Informations contenues dans un programme destiné à d'autres programmeurs (ou à toute personne lisant le code source) et n'ayant aucun effet sur l'exécution du programme.

- **erreur de syntaxe:** Une erreur dans un programme qui rend impossible l'analyse (et donc impossible à interpréter).

- **exception:** Une erreur détectée pendant l'exécution du programme.

- **sémantique:** Le sens d'un programme.

- **erreur sémantique:** Une erreur dans un programme qui lui fait faire autre chose que ce que le programmeur avait prévu.

### 2.10 Exercices

** Exercice 1 **

_Répétant les conseils du chapitre précédent, chaque fois que vous apprenez une nouvelle fonctionnalité, vous devriez l'essayer en mode interactif et faire des erreurs exprès pour voir ce qui ne va pas._

- _Nous avons vu que ```n = 42``` est légal. Qu'en est-il de ```42 = n``` ?_

- _Comment à propos de ```x = y = 1```?_

- _Dans certaines langues, chaque instruction se termine par un point-virgule,;. Que se passe-t-il si vous mettez un point-virgule à la fin d'une instruction Python?_

- _Que se passe-t-il si vous mettez un point à la fin d'une déclaration?_

- _En notation mathématique, vous pouvez multiplier x et y comme ceci: ```x y```. Que se passe-t-il si vous essayez cela en Python?_

** Exercice 2 **

_Pratique utilisant l'interpréteur Python comme calculatrice:_

1. _Le volume d'une sphère de rayon r est 4/3 π r<sup>3</sup>. Quel est le volume d'une sphère de rayon 5?_

2. _Supposez que le prix de vente d'un livre est de $24,95 , mais les librairies bénéficient d'une réduction de 40%. La livraison coûte $3 pour le premier exemplaire et 75 cents pour chaque exemplaire supplémentaire. Quel est le prix en gros total pour 60 exemplaires?_

3. _Si je quitte ma maison à 6h52 du matin et que je cours 1 mile à un rythme lent (8:15 par mile), puis 3 miles au tempo (7:12 par mile) et à un mile à nouveau, quelle heure puis-je rentrer à la maison pour le petit déjeuner?_ 

<hr>

# Chapitre 3<a name="ch3"></a>

## Les fonctions
<br><br>

Dans le contexte de la programmation, une fonction est une séquence d'instructions nommée qui effectue un calcul. Lorsque vous définissez une fonction, vous spécifiez le nom et la séquence d'instructions. Plus tard, vous pourrez “appeler” la fonction par son nom.

### 3.1 Appels de fonction

Nous avons déjà vu un exemple d'appel de fonction:

```python
>>> type (42)
<classe 'int'>
```

Le nom de la fonction est type. L'expression entre parenthèses est appelée l'argument de la fonction. Le résultat, pour cette fonction, est le type de l'argument.

Il est courant de dire qu'une fonction "prend" un argument et "renvoie" un résultat. Le résultat s'appelle également la valeur de retour.

Python fournit des fonctions qui convertissent les valeurs d'un type à un autre. La fonction int prend n'importe quelle valeur et la convertit en un entier, si elle le peut, ou se plaint sinon:

```python
>>> int('32')
32
>>> int('Hello')
ValueError: invalid literal for int(): Hello
```
int peut convertir les valeurs en virgule flottante en nombres entiers, mais cela n’arrondit pas; il coupe la partie fraction:

```python
>>> int(3.99999)
3
>>> int(-2.3)
-2
```

float convertit les entiers et les chaînes en nombres à virgule flottante:

```python
>>> float(32)
32.0
>>> float('3.14159')
3.14159
```

Enfin, str convertit son argument en chaîne:

```python
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
```

### 3.2 Fonctions mathématiques

Python a un module mathématique qui fournit la plupart des fonctions mathématiques habituelles. Un module est un fichier contenant une collection de fonctions connexes.

Avant de pouvoir utiliser les fonctions d'un module, nous devons l'importer avec une instruction import:

```python
>>> import math
```
Cette instruction crée un objet module nommé math. Si vous affichez l'objet module, vous obtenez des informations à ce sujet:

```python
>>> math
<module 'math' (built-in)>
```
L'objet module contient les fonctions et les variables définies dans le module. Pour accéder à l'une des fonctions, vous devez spécifier le nom du module et le nom de la fonction, séparés par un point (également appelé période). Ce format s'appelle la notation par point.

```python
>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)

>>> radians = 0.7
>>> height = math.sin(radians)
```
Le premier exemple utilise math.log10 pour calculer un rapport signal sur bruit en décibels (en supposant que signal_power et noise_power soient définis). Le module mathématique fournit également un journal, qui calcule les logarithmes de base e.

Le deuxième exemple trouve le sinus de radians. Le nom de la variable est un indice que péché et les autres fonctions trigonométriques (cos, tan, etc.) prennent des arguments en radians. Pour convertir des degrés en radians, divisez par 180 et multipliez par π:

```python
>>> degrees = 45
>>> radians = degrees / 180.0 * math.pi
>>> math.sin(radians)
0.707106781187
```

L'expression math.pi obtient la variable pi du module mathématique. Sa valeur est une approximation à virgule flottante de π, précise à environ 15 chiffres.

Si vous connaissez la trigonométrie, vous pouvez vérifier le résultat précédent en le comparant à la racine carrée de deux divisée par deux:

```python
>>> math.sqrt(2) / 2.0
0.707106781187
```

### 3.3 Composition

Jusqu'à présent, nous avons examiné les éléments d'un programme - variables, expressions et déclarations - de manière isolée, sans parler de la façon de les combiner.

Une des caractéristiques les plus utiles des langages de programmation est leur capacité à prendre et à composer de petits blocs de construction. Par exemple, l'argument d'une fonction peut être n'importe quel type d'expression, y compris les opérateurs arithmétiques:

```python
x = math.sin (degrés / 360.0 * 2 * math.pi)
```

Et même des appels de fonction:

```python
x = math.exp(math.log(x+1))
```

Presque n'importe où vous pouvez mettre une valeur, vous pouvez mettre une expression arbitraire, à une exception près: le côté gauche d'une instruction d'affectation doit être un nom de variable. Toute autre expression à gauche est une erreur de syntaxe (nous verrons des exceptions à cette règle plus tard).

```python
>>> minutes = hours * 60                 # right
>>> hours * 60 = minutes                 # wrong!
SyntaxError: can't assign to operator
```

### 3.4 Ajouter de nouvelles fonctions

Jusqu'à présent, nous utilisions uniquement les fonctions fournies avec Python, mais il est également possible d'ajouter de nouvelles fonctions. Une définition de fonction spécifie le nom d'une nouvelle fonction et la séquence d'instructions qui s'exécutent lorsque la fonction est appelée.

Voici un exemple:

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
```

def est un mot clé qui indique qu'il s'agit d'une définition de fonction. Le nom de la fonction est print_lyrics. Les règles pour les noms de fonction sont les mêmes que pour les noms de variables: les lettres, les chiffres et les traits de soulignement sont légaux, mais le premier caractère ne peut pas être un nombre. Vous ne pouvez pas utiliser un mot-clé comme nom d'une fonction et vous devez éviter d'avoir une variable et une fonction du même nom.

Les parenthèses vides après le nom indiquent que cette fonction ne prend aucun argument.

La première ligne de la définition de fonction s'appelle l'en-tête. le reste s'appelle le corps. L'en-tête doit se terminer par un deux-points et le corps doit être mis en retrait. Par convention, l'indentation est toujours de quatre espaces. Le corps peut contenir n'importe quel nombre d'énoncés.

Les chaînes dans les instructions d'impression sont placées entre guillemets. Les guillemets simples et les guillemets doubles font la même chose; la plupart des gens utilisent des guillemets simples, sauf dans les cas comme celui-ci où un guillemet simple (qui est aussi une apostrophe) apparaît dans la chaîne.

Tous les guillemets (simples et doubles) doivent être des «guillemets droits», généralement situés à côté de la touche Entrée du clavier. Les «guillemets bouclés», comme ceux de cette phrase, ne sont pas légaux en Python.

Si vous tapez une définition de fonction en mode interactif, l’interprète imprime des points (...) pour vous informer que la définition n’est pas complète:

```python
>>> def print_lyrics():
...     print("I'm a lumberjack, and I'm okay.")
...     print("I sleep all night and I work all day.")
...
```

Pour terminer la fonction, vous devez entrer une ligne vide.

La définition d'une fonction crée un objet de fonction, qui a le type fonction:

```python
>>> print(print_lyrics)
<function print_lyrics at 0xb7e99e9c>
>>> type(print_lyrics)
<class 'function'>
```

La syntaxe pour appeler la nouvelle fonction est la même que pour les fonctions intégrées:

```python
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```

Une fois que vous avez défini une fonction, vous pouvez l’utiliser dans une autre fonction. Par exemple, pour répéter le refrain précédent, nous pourrions écrire une fonction appelée repeat_lyrics:

```python
def repeat_lyrics ():
    print_lyrics ()
    print_lyrics ()
```

Et ensuite, appelez repeat_lyrics:

```python
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
```

Mais ce n’est pas vraiment comme ça que la chanson se passe.

### 3.5 Définitions et utilisations

En rassemblant les fragments de code de la section précédente, l'ensemble du programme se présente comme suit:

```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
```

Ce programme contient deux définitions de fonction: print_lyrics et repeat_lyrics. Les définitions de fonctions sont exécutées exactement comme les autres instructions, mais l’effet consiste à créer des objets de fonction. Les instructions à l'intérieur de la fonction ne sont exécutées que lorsque la fonction est appelée et que la définition de la fonction ne génère aucune sortie.

Comme vous vous en doutez, vous devez créer une fonction avant de pouvoir l'exécuter. En d'autres termes, la définition de la fonction doit être exécutée avant que la fonction ne soit appelée.

En tant qu'exercice, déplacez la dernière ligne de ce programme vers le haut pour que l'appel de fonction apparaisse avant les définitions. Exécutez le programme et voyez quel message d'erreur vous obtenez.

Déplacez maintenant l'appel de fonction vers le bas et déplacez la définition de print_lyrics après la définition de repeat_lyrics. Que se passe-t-il lorsque vous exécutez ce programme?

### 3.6 Flux d'exécution

Pour vous assurer qu'une fonction est définie avant sa première utilisation, vous devez connaître le déroulement des instructions, appelé flux d'exécution.

L'exécution commence toujours à la première déclaration du programme. Les instructions sont exécutées une par une, de haut en bas.

Les définitions de fonction ne modifient pas le flux d’exécution du programme, mais rappelez-vous que les instructions contenues dans la fonction ne sont exécutées que lorsque la fonction est appelée.

Un appel de fonction est comme un détour dans le flux d'exécution. Au lieu de passer à l'instruction suivante, le flux saute dans le corps de la fonction, y exécute les instructions, puis revient à la position où elle s'est arrêtée.

Cela semble assez simple, jusqu'à ce que vous vous souveniez qu'une fonction peut en appeler une autre. Au milieu d'une fonction, le programme peut devoir exécuter les instructions dans une autre fonction. Ensuite, lors de l’exécution de cette nouvelle fonction, le programme devra peut-être exécuter une autre fonction encore!

Heureusement, Python sait bien où il se trouve. Ainsi, chaque fois qu'une fonction est terminée, le programme reprend là où il l'avait laissé dans la fonction qui l'a appelée. Quand il arrive à la fin du programme, il se termine.

En résumé, lorsque vous lisez un programme, vous ne voulez pas toujours lire de haut en bas. Parfois, il est plus logique de suivre le déroulement de l’exécution.

### 3.7 Paramètres et arguments

Certaines des fonctions que nous avons vues nécessitent des arguments. Par exemple, lorsque vous appelez math.sin, vous passez un nombre en argument. Certaines fonctions prennent plus d'un argument: math.pow en prend deux, la base et l'exposant.

Dans la fonction, les arguments sont affectés à des variables appelées paramètres. Voici une définition pour une fonction qui prend un argument:

```python
def print_twice(bruce):
    print(bruce)
    print(bruce)
```

Cette fonction assigne l'argument à un paramètre nommé bruce. Lorsque la fonction est appelée, elle affiche deux fois la valeur du paramètre (quel qu’il soit).

Cette fonction fonctionne avec toutes les valeurs pouvant être imprimées.

```python
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(42)
42
42
>>> print_twice(math.pi)
3.14159265359
3.14159265359
```
Les mêmes règles de composition qui s'appliquent aux fonctions intégrées s'appliquent également aux fonctions définies par le programmeur. Nous pouvons donc utiliser n'importe quel type d'expression comme argument pour print_twice:

```python
>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
```
L'argument est évalué avant l'appel de la fonction. Ainsi, dans les exemples, les expressions 'Spam' * 4 et math.cos (math.pi) ne sont évaluées qu'une seule fois.

Vous pouvez également utiliser une variable comme argument:

```python
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
```
Le nom de la variable que nous passons en tant qu'argument (michael) n'a rien à voir avec le nom du paramètre (bruce). Peu importe que la valeur ait été appelée à la maison (dans l'appelant); ici à print_twice, nous appelons tout le monde bruce.

### 3.8 Les variables et les paramètres sont locaux

Lorsque vous créez une variable dans une fonction, elle est locale, ce qui signifie qu'elle n'existe que dans la fonction. Par exemple:

```python
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
```

Cette fonction prend deux arguments, les concatène et affiche le résultat deux fois. Voici un exemple qui l'utilise:

```python
>>> line1 = 'Bing tiddle '
>>> line2 = 'tiddle bang.'
>>> cat_twice(line1, line2)
Bing tiddle tiddle bang.
Bing tiddle tiddle bang.
```

Lorsque cat_twice se termine, la variable cat est détruite. Si nous essayons de l'imprimer, nous obtenons une exception:

```python
>>> print(cat)
NameError: name 'cat' is not defined
```

Les paramètres sont également locaux. Par exemple, en dehors de print_twice, il n’existe pas de bruce.

### 3.9 Diagrammes de pile

Pour savoir quelles variables peuvent être utilisées où, il est parfois utile de dessiner un diagramme de pile. Comme les diagrammes d'état, les diagrammes de pile indiquent la valeur de chaque variable, mais ils indiquent également la fonction à laquelle appartient cette variable.

Chaque fonction est représentée par un cadre. Un cadre est une boîte avec le nom d'une fonction à côté, ainsi que les paramètres et les variables de la fonction qu'il contient. Le diagramme de pile de l'exemple précédent est présenté à la figure 3.1.

![fig3.1](assets/tp3.1.png)

Figure 3.1: diagramme de pile.

Les cadres sont disposés dans une pile qui indique quelle fonction est appelée, et ainsi de suite. Dans cet exemple, print_twice a été appelé par cat_twice et cat_twice par __main__, qui est un nom spécial pour la plus haute image. Lorsque vous créez une variable en dehors de toute fonction, elle appartient à __main__.


Chaque paramètre fait référence à la même valeur que son argument correspondant. Ainsi, part1 a la même valeur que line1, part2 a la même valeur que line2 et bruce a la même valeur que cat.

Si une erreur se produit pendant un appel de fonction, Python affiche le nom de la fonction, le nom de la fonction qui l’a appelée et le nom de la fonction qui l’a appelée, jusqu’à __main__.

Par exemple, si vous essayez d'accéder à cat depuis print_twice, vous obtenez une erreur NameError:

```python
Traceback (innermost last):
  File "test.py", line 13, in __main__
    cat_twice(line1, line2)
  File "test.py", line 5, in cat_twice
    print_twice(cat)
  File "test.py", line 9, in print_twice
    print(cat)
NameError: name 'cat' is not defined
```

Cette liste de fonctions s'appelle un traceback. Il vous indique dans quel fichier de programme l'erreur s'est produite, dans quelle ligne et quelles fonctions étaient exécutées à ce moment-là. Il montre également la ligne de code qui a provoqué l'erreur.

L'ordre des fonctions dans le suivi est le même que celui des images dans le diagramme de pile. La fonction en cours d'exécution est en bas.

### 3.10 Fonctions fructueuses et fonctions vides

Certaines des fonctions que nous avons utilisées, telles que les fonctions mathématiques, renvoient des résultats; faute de meilleur nom, je les appelle des fonctions fructueuses. D'autres fonctions, comme print_twice, effectuent une action mais ne renvoient pas de valeur. Ils s'appellent des fonctions vides.

Lorsque vous appelez une fonction fructueuse, vous voulez presque toujours faire quelque chose avec le résultat; Par exemple, vous pouvez l'assigner à une variable ou l'utiliser dans le cadre d'une expression:

```python
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
```

Lorsque vous appelez une fonction en mode interactif, Python affiche le résultat:

```python
>>> math.sqrt(5)
2.2360679774997898
```

Mais dans un script, si vous appelez une fonction fructueuse toute seule, la valeur de retour est perdue à jamais!

```python
math.sqrt(5)
```

Ce script calcule la racine carrée de 5, mais comme il ne stocke ni n’affiche le résultat, il n’est pas très utile.

Les fonctions d'annulation peuvent afficher quelque chose à l'écran ou avoir un autre effet, mais elles n'ont pas de valeur de retour. Si vous affectez le résultat à une variable, vous obtenez une valeur spéciale appelée Aucune.

```python
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
```

La valeur None est différente de la chaîne "None". C'est une valeur spéciale qui a son propre type:

```python
>>> type(None)
<class 'NoneType'>
```

Les fonctions que nous avons écrites jusqu'à présent sont toutes nulles. Nous allons commencer à écrire des fonctions fructueuses dans quelques chapitres.

### 3.11 Pourquoi les fonctions?

On ne comprend peut-être pas pourquoi il vaut la peine de diviser un programme en fonctions. Il existe plusieurs raisons:

- La création d'une nouvelle fonction vous permet de nommer un groupe d'instructions, ce qui facilite la lecture et le débogage de votre programme.

- Les fonctions peuvent rendre un programme plus petit en éliminant le code répétitif. Plus tard, si vous effectuez un changement, vous ne devez le faire qu’à un seul endroit.

- Diviser un programme long en fonctions vous permet de déboguer les pièces une par une, puis de les assembler en un ensemble fonctionnel.

- Des fonctions bien conçues sont souvent utiles pour de nombreux programmes. Une fois que vous avez écrit et débogué, vous pouvez le réutiliser.

### 3.12 Débogage

Une des compétences les plus importantes que vous allez acquérir est le débogage. Bien que cela puisse être frustrant, le débogage est l’une des parties de la programmation les plus riches, les plus stimulantes et les plus intéressantes sur le plan intellectuel.

À certains égards, le débogage est comme un travail de détective. Vous êtes confronté à des indices et vous devez en déduire les processus et les événements qui ont conduit aux résultats que vous voyez.

Le débogage est aussi une science expérimentale. Une fois que vous avez une idée de ce qui ne va pas, modifiez votre programme et essayez à nouveau. Si votre hypothèse était correcte, vous pouvez prédire le résultat de la modification et vous rapprocher d'un programme opérationnel. Si votre hypothèse était fausse, vous devez en inventer une nouvelle. Comme Sherlock Holmes l'a souligné, "lorsque vous avez éliminé l'impossible, tout ce qui reste, aussi invraisemblable soit-il, doit être la vérité." (A. Conan Doyle, _The Sign of Four_)

Pour certaines personnes, la programmation et le débogage sont la même chose. C'est-à-dire que la programmation est le processus de débogage progressif d'un programme jusqu'à ce qu'il fasse ce que vous voulez. L'idée est que vous devriez commencer avec un programme fonctionnel et apporter de petites modifications, en les corrigeant au fur et à mesure.

Par exemple, Linux est un système d’exploitation qui contient des millions de lignes de code, mais c’était à l’origine un simple programme utilisé par Linus Torvalds pour explorer la puce Intel 80386. Selon Larry Greenfield, «L’un des projets précédents de Linus était un programme qui basculerait entre l’impression AAAA et BBBB. Ceci a ensuite évolué vers Linux. ”(_The Linux Users’ Guide_ Beta Version 1).

### 3.13 Glossaire

- **une fonction:** Une séquence d'instructions nommée qui effectue une opération utile. Les fonctions peuvent ou non prendre des arguments et peuvent ou non produire un résultat.

- **définition de la fonction:** Une instruction qui crée une nouvelle fonction, spécifiant son nom, ses paramètres et les instructions qu’elle contient.

- **objet de fonction:** Une valeur créée par une définition de fonction. Le nom de la fonction est une variable qui fait référence à un objet fonction.

- **entête:** La première ligne d'une définition de fonction.

- **corps:** La séquence d'instructions à l'intérieur d'une définition de fonction.

- **paramètre:** Un nom utilisé dans une fonction pour faire référence à la valeur transmise en tant qu'argument.

- **appel de fonction:** Une déclaration qui exécute une fonction. Il se compose du nom de la fonction suivi d'une liste d'arguments entre parenthèses.

- **argument:** Une valeur fournie à une fonction lorsque cette fonction est appelée. Cette valeur est affectée au paramètre correspondant dans la fonction.

- **variable locale:** Une variable définie dans une fonction. Une variable locale ne peut être utilisée que dans sa fonction.

- **valeur de retour:** Le résultat d'une fonction. Si un appel de fonction est utilisé comme expression, la valeur renvoyée est la valeur de l'expression.

- **fonction fructueuse:** Une fonction qui retourne une valeur.

- **fonction vide:** Une fonction qui renvoie toujours None.

- **Aucun:** Une valeur spéciale renvoyée par les fonctions void.

- **module:** Un fichier qui contient une collection de fonctions connexes et d'autres définitions.

- **déclaration d'importation:** Une instruction qui lit un fichier de module et crée un objet de module.

- **objet module:** Une valeur créée par une instruction d'importation qui donne accès aux valeurs définies dans un module.

- **notation par points:** La syntaxe pour appeler une fonction dans un autre module en spécifiant le nom du module suivi d'un point (point) et du nom de la fonction.

- **composition:** Utilisation d'une expression dans le cadre d'une expression plus grande ou d'une instruction dans le cadre d'une instruction plus grande

- **flux d'exécution:** Les instructions de commande sont exécutées.

- **diagramme de pile:** Représentation graphique d'une pile de fonctions, de leurs variables et des valeurs auxquelles elles se rapportent.

- **cadre:** Un cadre dans un diagramme de pile qui représente un appel de fonction. Il contient les variables locales et les paramètres de la fonction.

- **traceback:** Une liste des fonctions en cours d’exécution imprimées lorsqu’une exception se produit.

### 3.14 exercices

** Exercice 1 **

_Ecrivez une fonction nommée right_justify qui prend une chaîne nommée s en tant que paramètre et imprime la chaîne avec suffisamment d'espaces de début pour que la dernière lettre de la chaîne soit dans la colonne 70 de l'affichage._

```python
>>> right_justify('monty')
                                                                 monty
```

_Astuce: Utilisez la concaténation et la répétition de chaînes. En outre, Python fournit une fonction intégrée appelée len qui renvoie la longueur d'une chaîne. La valeur de len ('monty') est donc 5._

** Exercice 2 **

_Un objet fonction est une valeur que vous pouvez affecter à une variable ou transmettre sous forme d'argument. Par exemple, do_twice est une fonction qui prend un objet fonction en argument et l'appelle deux fois:_

```python
def do_twice(f):
    f()
    f()
```

Voici un exemple qui utilise do_twice pour appeler une fonction nommée print_spam deux fois.

```python
def print_spam():
    print('spam')

do_twice(print_spam)
```

1. _Tapez cet exemple dans un script et testez-le._

2. _Modifiez do_twice pour qu'il prenne deux arguments, un objet fonction et une valeur, et appelle la fonction deux fois, en transmettant la valeur sous forme d'argument._

3. _Copiez la définition de print_twice de ce chapitre dans votre script._ 

4. _Utilisez la version modifiée de do_twice pour appeler print_twice deux fois, en transmettant "spam" en tant qu'argument._

5. _Définissez une nouvelle fonction appelée do_four qui prend un objet fonction et une valeur et appelle la fonction quatre fois, en transmettant la valeur en tant que paramètre. Il ne devrait y avoir que deux déclarations dans le corps de cette fonction, pas quatre.
Solution: [http://thinkpython2.com/code/do_four.py](http://thinkpython2.com/code/do_four.py)._

** Exercice 3 **

_Remarque: Cet exercice doit être effectué à l'aide des déclarations et autres fonctionnalités que nous avons apprises jusqu'à présent._

_Ecrivez une fonction qui dessine une grille comme suit:_
```
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
```
_Astuce: pour imprimer plusieurs valeurs sur une ligne, vous pouvez imprimer une séquence de valeurs séparées par des virgules:_

```python
print ('+', '-')
```

Par défaut, print avance à la ligne suivante, mais vous pouvez remplacer ce comportement et mettre un espace à la fin, comme ceci:

```python
print('+', end=' ')
print('-')
```
_La sortie de ces instructions est "+ -" sur la même ligne. La sortie de la prochaine instruction print commencerait à la ligne suivante._

_Ecrivez une fonction qui dessine une grille similaire avec quatre lignes et quatre colonnes.
Solution: [http://thinkpython2.com/code/grid.py](http://thinkpython2.com/code/grid.py). Crédit: Cet exercice est basé sur un exercice de Oualline, Practical C Programming, Third Edition, O’Reilly Media, 1997._