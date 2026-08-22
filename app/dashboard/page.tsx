import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { employees } from "@/lib/data";

const statusColor = {
  present: "bg-green-500",
  leave: "bg-orange-500",
  absent: "bg-red-500",
};

export default function DashboardPage() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-semibold mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        {employees.map((emp) => (
          <Link key={emp.id} href={`/profile/${emp.id}`}>
            <Card className="hover:shadow-md transition-shadow cursor-pointer relative">
              <span
                className={`absolute top-3 right-3 w-3 h-3 rounded-full ${statusColor[emp.status]}`}
              />
              <CardContent className="flex flex-col items-center text-center gap-2 pt-6">
                <Avatar className="h-16 w-16">
                  <AvatarFallback>
                    {emp.name.split(" ").map((n) => n[0]).join("")}
                  </AvatarFallback>
                </Avatar>
                <p className="font-medium">{emp.name}</p>
                <p className="text-sm text-muted-foreground">{emp.designation}</p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}