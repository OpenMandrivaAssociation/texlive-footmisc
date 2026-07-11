%global tl_name footmisc
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	7.0b
Release:	%{tl_revision}.1
Summary:	A range of footnote options
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/footmisc
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of ways to change the typesetting of footnotes. The package
provides means of changing the layout of the footnotes themselves
(including setting them in 'paragraphs' -- the para option), a way to
number footnotes per page (the perpage option), to make footnotes
disappear in a 'moving' argument (stable option) and to deal with
multiple references to footnotes from the same place (multiple option).
The package also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the package are
overlap with the functionality of other packages. The para option is
also provided by the manyfoot and bigfoot packages, though those are
both also portmanteau packages. (Don't be seduced by fnpara, whose
implementation is improved by the present package.) The perpage option
is also offered by footnpag and by the rather more general-purpose
perpage

