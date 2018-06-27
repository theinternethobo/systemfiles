set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" The following are examples of different formats supported.
" Put Plugins after this line
" All of your Plugins must be added before the following line
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" set nocompatible					" use vim improvements
set autoindent						" automatically indent new lines...
set smartindent						" ...smartly
set backspace=2						" allow backspace over everything
set tabstop=6						" tabs are 8 characters
set nomodeline						" don't overwrite own .vimrc
set ignorecase          				" searches are case-insensitive...
set smartcase           				" ...unless they contain upper-case characters
set wrapscan						" wrap searches
set hlsearch						" highlight searches...
noremap <silent> <Space> :silent noh<Bar>echo<CR>	" ...but clear them with :space:
hi search ctermbg=red ctermfg=white			" highlight searches white on red
set nowrap						" don't wrap lines
setlocal comments-=://					" don't automatically comment
set nobackup						" don't use backup files...
set nowritebackup					" ...and don't create them
set ruler						" show the cursor
set showmatch						" highlight matching brackets
set history=500						" keep 500 lines of history
"syntax off						" turn off syntax highlighting

" use an informative status line...
set statusline=%F%m%r%h%w\ \[FORMAT=%{&ff}\]\ [TYPE=%Y]\ [ASCII=\%03.3b]\ [HEX=\%02.2B]\ [POS=%04l,%04v][%p%%]\ [LEN=%L]
set laststatus=2					" ...and always show it
set number
set mouse=a
colo koehler
"set gdefault          					" assume /g (global) on substitutions
"
"
