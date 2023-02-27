;; domain file: spazza-domain.pddl

(define (domain spazza-domain)

    (:requirements :strips :fluents :durative-actions :typing)

    ;; Types ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    (:types
        robot garbage box tile bin
    );; end Types ;;;;;;;;;;;;;;;;;;;;;;;;;    

    (:predicates
        (at_rob ?r - robot ?t - tile)
        (at_gar ?g - garbage ?t - tile)
        (at_box ?b - box ?t - tile)
        (at_bin ?b - bin ?t - tile)
        (free ?r - robot)
        (adjacent ?t1 - tile ?t2 - tile)
        (walkable ?t - tile)
        (holding ?r - robot ?g - garbage)
        (deleted ?g - garbage)
        (to_recycle ?g - garbage)
        (busy ?r - robot)
        (not_busy ?r - robot)
    )

    (:durative-action move
        :parameters (?r - robot ?from ?to - tile)
        :duration (= ?duration 3)
        :condition (and 
            (at start (at_rob ?r ?from))
            (over all (adjacent ?from ?to))
            (over all (walkable ?to))
            (at start (not_busy ?r))
        )
        :effect (and
            (at start (not(at_rob ?r ?from)))
            (at start (at_rob ?r ?to))
            (at start (not(not_busy ?r)))
            (at end (not_busy ?r))
        )
    )

    (:durative-action pickup
        :parameters (?r - robot ?t - tile ?g - garbage)
        :duration (= ?duration 1)
        :condition (and
            (at start (at_gar ?g ?t))
            (at start (at_rob ?r ?t))
        )
        :effect (and
            (at end (not(at_gar ?g ?t)))
            (at end (holding ?r ?g))
            (at start (not(not_busy ?r)))
            (at end (not_busy ?r))
        )
    )

    (:durative-action putdown
        :parameters (?r - robot ?t - tile ?b - bin ?g - garbage)
        :duration (= ?duration 1)
        :condition (and
            (over all (at_bin ?b ?t))
            (over all (at_rob ?r ?t))
            (at start (holding ?r ?g))
            (at start (not_busy ?r))
        )
        :effect (and
            (at end(at_gar ?g ?t))
            (at end (not(holding ?r ?g)))
            (at start (not(not_busy ?r)))
            (at end (not_busy ?r))
        )
    )
)