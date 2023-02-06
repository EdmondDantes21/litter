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
    )

    (:durative-action move
        :parameters (?r - robot ?from ?to - tile)
        :duration (= ?duration 3)
        :condition (and 
            (at start (at_rob ?r ?from))
            (over all (adjacent ?from ?to))
            (over all (walkable ?to))
        )
        :effect (and
            (at start (not(at_rob ?r ?from)))
            (at end (at_rob ?r ?to))
        )
    )

    (:durative-action pickup
        :parameters (?r - robot ?t - tile ?g - garbage)
        :duration (= ?duration 1)
        :condition (and
            (at start(free ?r))
            (at start (at_gar ?g ?t))
            (at start (at_rob ?r ?t))
        )
        :effect (and
            (at end (not(free ?r)))
            (at end (not(at_gar ?g ?t)))
            (at end (holding ?r ?g))
        )
    )

    (:durative-action putdown
        :parameters (?r - robot ?t - tile ?b - bin ?g - garbage)
        :duration (= ?duration 1)
        :condition (and
            (over all (at_bin ?b ?t))
            (over all (at_rob ?r ?t))
            (at start (holding ?r ?g))
        )
        :effect (and
            (at end(free ?r))
            (at end(at_gar ?g ?t))
            (at end (not(holding ?r ?g)))
        )
    )
)