% Undirected graph.
edge(Y,X):- edge(X,Y).

% Choose the starting point.
1 { path(0,N,N): edge(N,_) } 1.

% Choose a path length.
1 { pathlen(1..100) } 1.
% Best model is the one with minimal path length.
#minimize{L:pathlen(L)}.

% For each step, choose the next edge to take in path
1 { path(N+1,X,Y): edge(X,Y) } 1:- path(N,_,X); N<Len ; pathlen(Len).

% All edges must be covered by the path.
:- edge(X,Y) ; not path(_,X,Y) ; not path(_,Y,X).

% Which node in path at particular step.
goto(N,S):- path(N,_,S).

#show.
#show goto/2.
