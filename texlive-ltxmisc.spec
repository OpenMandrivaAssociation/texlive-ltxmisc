%global tl_name ltxmisc
%global tl_revision 75878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Miscellaneous LaTeX packages, etc.
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/misc
License:	collection
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxmisc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Miscellaneous LaTeX packages, etc.

