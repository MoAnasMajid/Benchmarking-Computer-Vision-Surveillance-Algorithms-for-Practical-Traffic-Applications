%cd /content/TrackEval/scripts
!python run_mot_challenge.py --BENCHMARK ABC --SPLIT_TO_EVAL train --TRACKERS_TO_EVAL mytracker --METRICS HOTA Clear Identity VACE --USE_PARALLEL False --NUM_PARALLEL_CORES 1 --CLASSES_TO_EVAL pedestrian
