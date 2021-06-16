(let ((default-directory  "~/.config/emacs/.local/straight/build"))
  (normal-top-level-add-subdirs-to-load-path))
(require 'find-lisp)
(require 'ox-hugo)
(require 'org-id)
;; (require 'org-roam)
(require 'org-ref)
(setq org-roam-directory "~/Brain/org/")
(setq enable-local-variables nil)

(defun my--org-roam-publish (file)
  (with-current-buffer (find-file-noselect file)
    (setq org-hugo-base-dir "..")
    (let ((org-id-extra-files (find-lisp-find-files org-roam-directory "\.org$")))
      (org-hugo-export-wim-to-md))))
