% =====================================================================
%  conjura-solution.cls
%
%  House LaTeX class for Conjura solution/proof documents.  Inherits
%  the Conjura visual identity from conjura-conjecture.cls (fonts,
%  colors, theorem environments, running heads) but widens the page:
%  a solution is unbounded in length and typically carries long
%  derivations that the statement class's narrow 5x8in page cannot
%  comfortably hold.
%
%  The only structural requirement on a solution document is that it
%  name, at the top, which conjecture it resolves -- see \cjresolves
%  below.  Everything after that is free form: whatever sections,
%  theorem/lemma/proof environments, or appendices the proof needs.
% =====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{conjura-solution}[2026/08/15 v1.0 Conjura solution document class]
\LoadClass{conjura-conjecture}

% wider, book-trim page -- proofs run long and need room for display
% math that the statement class's narrow screen page cannot give them
\geometry{papersize={6.5in,9.25in},top=0.85in,bottom=0.85in,
  left=0.75in,right=0.75in,headheight=14pt,headsep=0.2in,footskip=0.4in}

% the one required piece of front matter: which conjecture this
% resolves
\newcommand{\cjresolves}[1]{\vspace{0.5em}\noindent{\small\textbf{Resolves.}%
  \ #1}\par}
