# ResolveTableaux
 Resolvedor de Tableaux feito em Python como projeto de faculdade

Forma de usar: 
Este Resolvedor de Tableaux apenas utiliza lógica proposicional, não se valendo de lógica de primeira ordem em diante. 
Proposições: ^ (e), v (ou), > (implica).
Negação: ~.
Queremos descobrir se uma fórmula é válida(todas as suas interpretações serão verdade para quaisquer valores booleanos de suas proposições), podemos construir da seguinte forma:
"A proposição p implica na proposição q":
(p>q)
Sempre deverá haver parênteses externos, englobando toda a construção. 
"p ou (q e r)":
(pv(q^r))
"p implica não(q ou r)"
(p>~(qvr))
O resultado responderá, caso seja inválida, uma forma de instanciar valores às variáveis para que o resultado seja falso. As proposições em maiúsculo são negações de suas minúsculas, por exemplo:
((pv(q^r))>(~(p>q)>(p^r)))
É inválida, e o programa acusará:[['R', 'Q', 'p', 'p']] como método de resolução. Note que, dentro deste array, há outro array. O array inicial será as respostas válidas, quaisquer array interior significa que aqueles valores devem ser usados simultaneamente. Neste exemplo, R, Q, p ,p (redundante), ou seja, p verdadeiro, q e r falsos resultará na proposição inicial sendo falsa. 