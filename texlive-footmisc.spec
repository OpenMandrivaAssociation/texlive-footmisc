# revision 23330
# category Package
# catalog-ctan /macros/latex/contrib/footmisc
# catalog-date 2011-06-09 17:50:36 +0200
# catalog-license lppl1.3
# catalog-version 5.5b
Name:		texlive-footmisc
Version:	5.5b
Release:	3
Summary:	A range of footnote options
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/footmisc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/footmisc.source.tar.xz
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
%{_texmfdistdir}/tex/latex/footmisc/footmisc.sty
%doc %{_texmfdistdir}/doc/latex/footmisc/README
%doc %{_texmfdistdir}/doc/latex/footmisc/footmisc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/footmisc/footmisc.dtx
%doc %{_texmfdistdir}/source/latex/footmisc/footmisc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.5b-2
+ Revision: 752050
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.5b-1
+ Revision: 718490
- texlive-footmisc
- texlive-footmisc
- texlive-footmisc
- texlive-footmisc

