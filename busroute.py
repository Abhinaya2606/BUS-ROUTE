#include<stdio.h>
#include<string.h>

void findRoutes (char bus[][30], char search[20])
{
  int c = 0, i, n = 25;


  for (i = 1; i < n; i++)
    {
      if (strcmp (bus[i], search) == 0)
	{
	  c = 1;

	  break;
	}

    }
  if (c == 1)
    printf ("\n %s ", bus[0]);
}

int main ()
{
  char stop[50];
  printf ("\n WELCOME TO *KNOW YOUR BUS* ");
  printf ("\n\n St.Joseph's Institute Of Technology");
  printf("\n\n 1.MAKE SURE YOU ENTER THE RIGHT SPELLING \n 2.NO SPACING AND USE LOWERCASE ONLY");
  printf ("\n\n Where do you want to go : ");
  scanf ("%s", stop);
  char t11[][30] =
    { "AVADI BUS", "avadi", "thirumalaivoyal", "ambattur", "annaarch",
"skywalk", "methanagar", "mogappair", "choolaimedu", "loyolacollege", "tnagar" };
  char t12[][30] =
    { "KOYAMBEDU BUS", "koyambedu", "koyambedutower",
"koyambedumajestictower", "jainagar", "mmda", "vadapalani", "vadapazhani",
"srinivasatheatre", "citnagar", "saidapet", "saidapetsignal", "chinnamalai" };
  char t13[][30] =
    { "RED HILLS BUS", "redhills", "kolathur", "annasilai", "annastatue",
"donboscoschool", "periyarnagar", "jawaharnagar", "agaram", "perambur", "otteri",
"madhyakailash", "srptools", "kandanchavadi", "perungudi" };
  char t14[][30] =
    { "MADHAVARAM BUS", "madhavaram", "thapalpetti", "moolakadai", "mrnagar",
"mullainagar", "ambedkarcollege", "vyasarpadi", "bhuvaneshwaritheatre", "dowtown",
"vepperi" };
  char t24[][30] =
    { "VILLIWAKKAM BUS", "villiwakkam", "villivakkam", "icf", "chindadripet",
"royapetta", "royapettah", "ajantha", "mylapore", "mylaporetank", "manthaveli",
"adyar", "adyartelephoneexchange", "rmhospital", "kottivakkam", "palavakkam",
"thiruvanmiyur" };
  char t31[][30] =
    { "THIRUVOTTIYUR BUS", "thiruvottiyur", "tiruvottiyur", "ajax",
"vellaiyannchettyschool", "thiruvottiyurmarket", "thearadi", "rajakadai", "kasimedu",
"kalmandapam", "royapuram", "triplicane", "rathnacafe", "icehouse", "lighthouse",
"santhome", "pattinapakkam", "mrcnagar", "thiruvanmiyur", "kottivakkam",
"palavakkam" };
  char t32[][30] =
    { "TONDIARPET BUS", "tondayarpet", "tondiarpet", "thandayarpet", "n4",
"agasthiya", "manigundu", "thiyagarajacollege", "mint", "broadway", "minerva",
"thiruvanmiyur", "neelangarai", "kottivakkam", "palavakkam", "vettuvankeni" };
  char t41[][30] =
    { "CHENGALPET BUS", "chengapet", "singaperumalkovil", "maraimalainagar",
"potheri", "guduvancherry", "urapakkam", "oorapakkam", "perungalathur", "tambaram",
"tambaramgate" };
  char t42[][30] =
    { "PALLAVARAM BUS", "pallavaram", "chrompet", "mit", "meps",
"ministerhouse", "camproad", "mahalakshminagar", "santhosapuram" };
  char t47[][30] =
    { "BALAJI NAGAR", "balajinagar", "eswanthnagar", "sudarsannagar",
"vgpambikagarden", "vgpgarden", "chembakkam", "gowrivakkam", "gowriwakkam" };
  char t51[][30] =
    { "POONAMALLE BUS", "poonamalle", "karaiyanchavadi", "karayanchavadi",
"kumanachavadi", "kattupakkam", "kaattupakkam", "iyyappanthangal", "sakthinagar",
"muglivakkam", "ramapuram", "buttroad", "guindy" };
  char t52[][30] =
    { "PORUR BUS", "porur", "baikadai", "mowlivakkam", "valasaravakkam",
"kesavarthini", "virugambakkam", "avichischool", "kasitheatre", "velacherry",
"velacherrybypass" };
  char t61[][30] =
    { "KALIAPPA HOSPITAL BUS", "kaliappa", "kaliappahospital", "mandaiveli",
"mandaveli", "ambikaappalam", "indranagar", "jaincollege", "thorapakkam", "ptc",
"karapakkam", "aavin", "kumarannagar", "palavakkam", "vettuvankeni", "kottivakkam",
"thiruvanmiyur" };
  char t62[][30] =
    { "K-4 BUS", "k4policestation", "senthilnagar", "annanagar",
"annanagarwest", "lotuscolony", "chinthamani", "kilpauk", "taylorsroad", "chetpet",
"tajhotel", "nanthanam", "kotturpuram", "iit" };
  char t81[][30] =
    { "N.G.O COLONY BUS ", "ngocolony", "puzhuthiwakkam", "puzhuthivakkam",
"mountrs", "bluebike", "skolathur" };
  char t82[][30] =
    { "NANGANALLUR BUS", "nanganallur", "palavanthangal", "pazhavanthangal",
"madipakkam", "kilkattalai", "keezhkattalai", "keelkattalai", "kovilampakkam" };
  char t91[][30] =
    { "BESANT NAGAR BUS", "besantnagar", "avvaihome", "rajajibhavan",
"spencer", "spencerplaza", "thiruvanmiyur", "palavakkam", "vettuvankeni",
"injambakkam", "kottivakkam", "neelangarai", "rmhospital" };
  char t100[][30] =
    { "KALPAKKAM BUS", "kalpakkam", "poocherry", "thiruporur", "kelambakkam",
"navalur" };
  char t40[][30] =
    { "KANCHIPURAM BUS", "kanchipuram", "walajabad", "padapai", "mudichur",
"krishnanagar", "cristking" };
  findRoutes (t11, stop);
  findRoutes (t12, stop);
  findRoutes (t13, stop);
  findRoutes (t14, stop);
  findRoutes (t24, stop);
  findRoutes (t31, stop);
  findRoutes (t32, stop);
  findRoutes (t41, stop);
  findRoutes (t42, stop);
  findRoutes (t47, stop);
  findRoutes (t51, stop);
  findRoutes (t52, stop);
  findRoutes (t61, stop);
  findRoutes (t62, stop);
  findRoutes (t81, stop);
  findRoutes (t82, stop);
  findRoutes (t91, stop);
  findRoutes (t100, stop);
  findRoutes (t40, stop);
  printf("\n\n\n\n\n\n NOTE: if no bus name is displayed please check your spelling and try again!");
  printf ("\n  OR we don't have buses there");
  return 0;
}
