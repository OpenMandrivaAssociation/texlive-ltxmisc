# revision 21927
# category Package
# catalog-ctan /macros/latex/contrib/misc
# catalog-date 2009-01-16 15:12:56 +0100
# catalog-license collection
# catalog-version undef
Name:		texlive-ltxmisc
Version:	20170414
Release:	1
Summary:	Miscellaneous LaTeX packages, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxmisc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ltxmisc package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxmisc/abstbook.cls
%{_texmfdistdir}/tex/latex/ltxmisc/beletter.cls
%{_texmfdistdir}/tex/latex/ltxmisc/bibcheck.sty
%{_texmfdistdir}/tex/latex/ltxmisc/concrete.sty
%{_texmfdistdir}/tex/latex/ltxmisc/flashcard.cls
%{_texmfdistdir}/tex/latex/ltxmisc/iagproc.cls
%{_texmfdistdir}/tex/latex/ltxmisc/linsys.sty
%{_texmfdistdir}/tex/latex/ltxmisc/mitpress.sty
%{_texmfdistdir}/tex/latex/ltxmisc/thrmappendix.sty
%{_texmfdistdir}/tex/latex/ltxmisc/topcapt.sty
%{_texmfdistdir}/tex/latex/ltxmisc/vrbexin.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090116-2
+ Revision: 753576
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090116-1
+ Revision: 718914
- texlive-ltxmisc
- texlive-ltxmisc
- texlive-ltxmisc
- texlive-ltxmisc

