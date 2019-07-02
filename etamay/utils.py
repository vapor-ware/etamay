
import logging


_log = logging.getLogger('etamay.utils')


def fuzzy_find(branches, tree):
    total = len(branches)

    if total == 1:
        return find_uri(branches[0], tree)

    c = 0
    branch = branches[0]

    while c < total:
        _log.debug('Fuzzing Branch: {} ({} / {})'.format(branch, c + 1, total))
        new_tree = find_uri(branch, tree)

        c += 1
        if new_tree:
            try:
                branch = branches[c]
            except IndexError:
                return new_tree

            tree = new_tree
            continue

        try:
            branch = '/'.join([branch, branches[c]])
        except IndexError:
            return new_tree


def find_uri(parts, tree):
    if not tree:
        return None

    if isinstance(parts, list):
        if len(parts) == 1:
            return tree.get(parts[0])

        return find_uri(parts[1:], tree.get(parts[0]))

    return tree.get(parts)
