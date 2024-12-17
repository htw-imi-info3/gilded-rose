
DO_REFACTORING = True

if DO_REFACTORING:
    from gilded_rose.refactored import GildedRose, Item
    # add the refactored types here one by one to use the fixed expectations in test/bug and test/new
    # example:
    # FIXED = ['sulfuras', 'aged_brie', 'normal', 'backstage', 'conjured']
    FIXED = [ ]




# use this to tests the test variants:
PREPARE_TESTS = not DO_REFACTORING
ORIGINAL_IMPLEMENTATION = False
if PREPARE_TESTS: 

    if ORIGINAL_IMPLEMENTATION:
        from gilded_rose.original import GildedRose, Item
        FIXED = [ ]
    else:
        from gilded_rose.refactoring_example import GildedRose, Item
        FIXED = ['sulfuras', 'aged_brie', 'normal', 'backstage', 'conjured']

