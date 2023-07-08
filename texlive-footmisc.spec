Name:		texlive-footmisc
Version:	67556
Release:	1
Summary:	A range of footnote options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footmisc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A collection of ways to change the typesetting of footnotes.
The package provides means of changing the layout of the
footnotes themselves (including setting them in 'paragraphs' --
the para option), a way to number footnotes per page (the
perpage option), to make footnotes disappear when an argument
moves (stable option) and to deal with multiple references to
footnotes from the same place (multiple option). The package
also has a range of techniques for labelling footnotes with
symbols rather than numbers. Some of the functions of the
package are overlap with the functionality of other packages.
The para option is also provided by the manyfoot and bigfoot
packages, though those are both also portmanteau packages.
(Don't be seduced by fnpara, whose implementation is improved
by the present package.) The perpage option is also offered by
footnpag and by the rather more general-purpose perpage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/footmisc
%doc %{_texmfdistdir}/doc/latex/footmisc
#- source
%doc %{_texmfdistdir}/source/latex/footmisc

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
