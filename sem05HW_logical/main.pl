/******************************************************************************

                            Online Prolog Compiler.
                Code, Compile, Run and Debug Prolog program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

% Сумма элементов пустого списка равна 0
sum([], 0).

% Если список не пустой:
% Складываем голову списка с суммой оставшейся части списка
sum([Head|Tail], Sum) :-
    sum(Tail, TempSum),
    Sum is Head + TempSum.

% Пример запуска:

?- sum([1, 2, 3, 4, 5], Sum), write(Sum).

