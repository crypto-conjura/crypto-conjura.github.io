% =====================================================================
%  conjura-conjecture.cls
%
%  House LaTeX class for Conjura conjecture-statement documents.
%  Carries the shared look and feel (fonts, page geometry, colors,
%  running heads, theorem-style environments) so that an individual
%  statement.tex only has to supply front-matter text and content.
%
%  Companion class: conjura-solution.cls, which \LoadClass{}es this
%  one and widens the page for long, unbounded proofs.
% =====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{conjura-conjecture}[2026/08/15 v1.0 Conjura conjecture statement class]
\LoadClass[10pt]{article}

% ---- fonts: Baskervald X text + matching math, Helvetica-like sans
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{amsmath,amsthm}
\RequirePackage[osf]{Baskervaldx}
\RequirePackage[baskervaldx,bigdelims]{newtxmath}
\RequirePackage[scaled=.92]{helvet}
\RequirePackage{microtype}
\linespread{1.0}
\frenchspacing

% ---- small "screen" page, generous leading
\RequirePackage[papersize={5in,8in},top=0.78in,bottom=0.72in,left=0.55in,
  right=0.55in,headheight=14pt,headsep=0.16in,footskip=0.32in]{geometry}

% ---- palette
\RequirePackage{xcolor}
\definecolor{cjAccent}{RGB}{224,142,27}   % headings, links, folios
\definecolor{cjBorder}{RGB}{247,214,148}  % definition-box frame
\definecolor{cjFill}{RGB}{253,242,215}    % conjecture/informal-box fill

\RequirePackage{enumitem}

% ---- section heads
\RequirePackage{titlesec}
\titleformat{\section}{\Large\bfseries}{\thesection}{0.7em}{}
\titlespacing*{\section}{0pt}{12pt plus 2pt minus 2pt}{5pt plus 1pt}

% ---- running heads: orange sans, folio top right; plain first page
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\newcommand{\cj@runninghead}{}
\newcommand{\runninghead}[1]{\renewcommand{\cj@runninghead}{#1}}
\fancyhead[L]{\color{cjAccent}\sffamily\footnotesize\cj@runninghead}
\fancyhead[R]{\color{cjAccent}\sffamily\bfseries\small\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}}
\AtBeginDocument{\thispagestyle{plain}}

\RequirePackage[most]{tcolorbox}

\RequirePackage[colorlinks=true,linkcolor=cjAccent,citecolor=cjAccent,
  urlcolor=cjAccent]{hyperref}
\RequirePackage{xurl}

% ---- theorem styles: bold heads, optional note in parentheses
\newtheoremstyle{cjplain}{5pt plus 1pt}{5pt plus 1pt}%
  {\itshape}{}{\bfseries}{.}{ }%
  {\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}
\newtheoremstyle{cjdef}{5pt plus 1pt}{5pt plus 1pt}%
  {\upshape}{}{\bfseries}{.}{ }%
  {\thmname{#1}\thmnumber{ #2}\thmnote{ (#3)}}

\theoremstyle{cjplain}
\newtheorem{conjecture}{Conjecture}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{cjdef}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}
% \begin{proof}...\end{proof} comes from amsthm; no redefinition needed.

% conjecture/definition get boxed; theorem/lemma/proposition/corollary/
% remark stay unboxed so a long proof document doesn't turn into a
% wall of boxes
\tcolorboxenvironment{definition}{enhanced jigsaw,breakable,
  sharp corners,boxrule=2pt,colframe=cjBorder,colback=white,
  left=5pt,right=5pt,top=2pt,bottom=2pt,
  before skip=6pt,after skip=6pt}
\tcolorboxenvironment{conjecture}{enhanced jigsaw,breakable,
  sharp corners,boxrule=0pt,frame hidden,colback=cjFill,
  left=6pt,right=6pt,top=4pt,bottom=4pt,
  before skip=6pt,after skip=6pt}

% ---- front-matter box for a one-paragraph informal restatement
\newtcolorbox{informalconjecture}[1][Conjecture (informal)]{%
  enhanced jigsaw,sharp corners,boxrule=0pt,frame hidden,colback=cjFill,
  left=6pt,right=6pt,top=4pt,bottom=4pt,
  before upper={\textbf{#1.}\ \itshape}}

% ---- bibliography: a numbered "Bibliography" \section heading with
% no duplicate \refname heading from thebibliography itself
\newenvironment{conjurabibliography}[1]{%
  \begingroup\small\renewcommand{\section}[2]{}%
  \begin{thebibliography}{#1}%
}{%
  \end{thebibliography}\endgroup
}

% ---- one-shot front-matter rendering commands
\newcommand{\cjkicker}[1]{\noindent{\sffamily\bfseries #1}\par}
\newcommand{\cjtitle}[1]{\vspace{0.6em}{\noindent\LARGE\itshape
  \color{cjAccent}#1\par}}
\newcommand{\cjsubtitle}[1]{\vspace{0.6em}\noindent{\itshape #1}\par}
\newcommand{\cjstatus}[1]{\vspace{0.5em}\noindent{\small\textbf{Status.}
  #1}\par}
\newcommand{\cjcategory}[1]{\smallskip\noindent{\small\textbf{Category.}
  #1}\par}

% ---- small conveniences used across Conjura conjecture write-ups
\newcommand{\poly}{\mathrm{poly}}
\newcommand{\sample}{\leftarrow}

\emergencystretch=1.5em
