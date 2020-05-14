import subprocess
import argparse
import sys

ADB_PATH = "adb"
USER = 0
VERBOSE = False
FAKE = False

apps = [
{
  "id": 1,
  "name": "Google chrome",
  "index": "com.android.chrome",
  "remove": True
},
{
  "id": 2,
  "name": "Mail",
  "index": "com.android.email",
  "remove": True
},
{
  "id": 3,
  "name": "Google quick search box",
  "index": "com.google.android.googlequicksearchbox",
  "remove": True
},
{
  "id": 4,
  "name": "Google play music",
  "index": "com.google.android.music",
  "remove": True
},
{
  "id": 5,
  "name": "Google play videos & TV",
  "index": "com.google.android.videos",
  "remove": True
},
{
  "id": 6,
  "name": "Google Duo",
  "index": "com.google.android.apps.tachyon",
  "remove": True
},
{
  "id": 7,
  "name": "MiDrop",
  "index": "com.xiaomi.midrop",
  "remove": True
},
{
  "id": 8,
  "name": "MIUI analytics",
  "index": "com.miui.analytics",
  "remove": True
},
{
  "id": 9,
  "name": "MIUI weather provider",
  "index": "com.miui.providers.weather",
  "remove": True
},
{
  "id": 10,
  "name": "MIUI weather",
  "index": "com.miui.weather2",
  "remove": True
},
{
  "id": 11,
  "name": "Screen recorder",
  "index": "com.miui.screenrecorder",
  "remove": True
},
{
  "id": 12,
  "name": "Mi video",
  "index": "com.miui.videoplayer",
  "remove": True
},
{
  "id": 13,
  "name": "Mi music",
  "index": "com.miui.player",
  "remove": True
}]


def count_remove(remove=True):
    ret = 0
    for app in apps:
        if app["remove"] == remove:
            ret += 1
    return ret


def print_app(app):
    print("%2i  %-24s  %s" % (app["id"], app["name"], app["index"]))


def print_apps():
    to_remove = count_remove(True)
    to_keep = count_remove(False)
    if to_remove != 0:
        print("\nApps to remove: %i" % to_remove)
        for app in apps:
            if app["remove"] == True:
                print_app(app)
    if to_keep != 0:
        print("\nApps to keep: %i" % to_keep)
        for app in apps:
            if app["remove"] == False:
                print_app(app)


def remove_apps():
    # todo check adb is working
    success = []
    not_installed = []
    fails = []

    for i, app in enumerate(apps):
        command = "%s shell pm uninstall --user %i %s" % (ADB_PATH, USER, app["index"])
        if VERBOSE:
            print("Executing command: %s" % command)
        else:
            sys.stdout.write("[%-*s]\r" % (to_remove, "#"*i))
            sys.stdout.flush()

        if not FAKE:
            out = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            result = out.communicate()[0]
            if result == "Success":
                success.append("%s" % app["name"])
            elif "not installed" in result:
                not_installed.append("%s" % app["name"])
            else:
                fails.append("%s: %s" % (app["name"], result))
        else:
            print("Fake!")

    if success:
        print("Successfully removed %i apps:" % len(success))
        for app in success:
            print("\t%s" % app)
    if not_installed:
        print("%i apps were not installed:" % len(not_installed))
        for app in not_installed:
            print("\t%s" % app)
    if fails:
        print("Failed to remove %i apps:" % len(fails))
        for app in fails:
            print("\t%s" % app)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove unwanted apps from a MIUI ROM.')
    parser.add_argument('--list', action='store_true',
                        help='print list of apps. Program exists after print.')
    parser.add_argument('--verbose', action='store_true',
                        help='print more information.')
    parser.add_argument('--fake', action='store_true',
                        help='Runn application without executing the commands.')
    parser.add_argument('--keep', nargs='+', type=int,
                        help="A list of the app IDs for apps you want to keep. User --print to see it IDs")

    args = parser.parse_args()

    if args.list:
        print_apps()
        exit()

    VERBOSE = args.verbose
    FAKE = args.fake

    # Set apps to keep
    if args.keep:
        new_apps = []
        for app in apps:
            if app["id"] in args.keep:
                app["remove"]=False
            new_apps.append(app)
        apps = new_apps

    print_apps()

    agreed = raw_input("Continue? [y/N]: " or "N")

    # Remove apps to be kept from the list
    to_remove = count_remove(True)
    if to_remove != len(apps):
        new_apps = []
        for app in apps:
            if app["remove"]:
                new_apps.append(app)
        apps = new_apps

    if agreed.lower() not in ["y", "yes"]:
        print("Exiting!")
        exit()

    remove_apps()
