Name:		texlive-ltxmisc
Version:	21927
Release:	2
Summary:	Miscellaneous LaTeX packages, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxmisc.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
