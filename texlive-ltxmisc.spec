Name:		texlive-ltxmisc
Version:	20090116
Release:	1
Summary:	Miscellaneous LaTeX packages, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc
License:	COLLECTION
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxmisc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive ltxmisc package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
